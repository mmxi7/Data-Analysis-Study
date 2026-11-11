from math import sqrt
from pandas import DataFrame
from scipy.stats import t
from scipy.stats import normaltest, bartlett, levene
from scipy.stats import ttest_1samp, wilcoxon

def ci(data, columns=None, clevel=0.95):
    """
    주어진 데이터에 대한 모평균의 신뢰구간을 계산하는 함수

    Args:
        data (Series | list | ndarray | DataFrame): 연속형 데이터 또는 데이터프레임
        column (str): data가 데이터프레임인 경우 대상 컬럼명 (기본값: None)

    Returns:
        tuple: (신뢰구간 하한, 신뢰구간 상한)
    """
    # 데이터프레임 + 컬럼명 형태로 전달된 경우 해당 컬럼만 추추
    if columns is not None:
        data = data[columns]

    n = len(data)                               # 표본 크기
    dof = n - 1                                 # 자유도
    sample_mean = data.mean()                   # 표본 평균
    sample_std = data.std()                     # 표본 표준오차
    sample_std_error = sample_std / sqrt(n)     # 표준 오차

    # 신뢰구간을 계산하여 리턴한다.
    return t.interval(clevel, dof, loc=sample_mean, scale=sample_std_error)





def test_assumptions(data, columns=None, alpha=0.05, center="median"):
    """
    가설검정의 가정(정규성, 등분산성)을 일괄적으로 검정하여 결과표를 반환하는 함수

    각 변수에 대해 정규성 검정(normaltest)을 수행하고, 변수가 두 개 이상인 경우
    등분산성 검정을 수행한다. 이때 모든 변수가 정규성을 충족하고 Bartlett 검정을,
    하나라도 충족하지 못하면 Levene 검정을 선택적으로 사용한다.

    Args:
        data (DataFrame): 검정 대상이 되는 데이터프레임
        columns (list): 검정에 사용할 컬럼명 목록 (기본값: None -> 수치형 컬럼 전체)
        alpha (float): 유의수준 (기본값: 0.05)
        center (str): Levene 검정 시 사용할 중심 경향값 (기본값: "median")

    Returns:
        DataFrame: field를 인덱스로 하는 검정 결과표
                  (test, statistic, p-value, result 컬럼 포함)
    """
    # 검정에 사용할 컬럼 결정 (지정하지 않으면 수치형 컬럼 전체 사용)
    if columns is None:
        columns = data.select_astype(include="number").columns.tolist()

    # 하나의 컬럼명이 문자열로 전달된 경우 리스트로 감싸준다
    if type(columns) == str:
        columns = [columns]

    report = []         # 결과를 누적할 리스트
    normal_dist = True  # 모든 변수가 정규성을 충족하는지 여부

    # 각 변수에 대한 정규성 검정
    for c in columns:
        # 결측치 제거 후 검정 (불균형 표본 대응)
        s, p = normaltest(data[c].dropna())
        normalize = p >= alpha

        report.append({
            "field": c,
            "test": "normaltest",
            "statistic": s,
            "p-value": p,
            "result": normalize
        })

        normal_dist = normal_dist and normalize

    # 변수가 두 개 이상인 경우 등분산성 검정
    if len(columns) > 1:
        # 각 컬럼을 결측 제거 후 실수형으로 변환하여 리스트로 추출 (Bartlett은 실수형 필요)
        samples = [data[c].dropna().astype("float") for c in columns]

        if normal_dist:     # 모든 변수가 정규성을 충족 -> Bartlett 검정
            name = "Bartlett"
            s, p = bartlett(*samples)
        else:               # 하나라도 정규성을 충족하지 못함 -> Levene 검정
            name = "Levene"
            s, p = levene(*samples, center=center)

        report.append({
            "field": name,
            "test": "equal_var",
            "statistic": s,
            "p-value": p,
            "result": p >= alpha
        })

    # 결과표 리턴
    return DataFrame(report).set_index("field")





def test_1sample(data, column, popmean=0, alpha=0.05):
    """
    한 집단의 평균이 기준값(popmean)과 같은지 검정하는 함수

    정규성 충족 시 일표본 t검정, 미충족 시 Wilcoxon 부호순위 검정을 수행하며,
    양측, 좌측단측, 우측단측 세 가지 대립가설을 일괄 검정한다.

    Args:
        data (DataFrame): 검정 대상 데이터프레임
        columns (str): 검정할 연속형 컬럼명
        popmean (float): 비교 기준이 되는 모평균 μ₀ (기본값: 0)
        alpha (float): 유의수준 (기본값: 0.05)

    Returns:
        DataFrame: 대립가설(alternative)별 검정, 통계량, p-value, 유의성 결과표
                   (two-sided / less / greater 3행)
    """
    # 대상 컬럼을 결측 제거하여 추출
    sample = data[[column]].dropna()

    # test_assumptions로 정규성 검정 (단일 컬럼이라 등분산성은 수행되지 않음)
    report = test_assumptions(sample, columns=column, alpha=alpha)

    # 정규성 충족 여부 추출
    is_normal = bool(report.loc[column, "result"])

    # 정규성 충족 여부에 따라 적용할 검정 이름 결정
    test_name = "One-sample t-test" if is_normal else "Wilcoxon signed-rank test"

    # 대립가설 방향별 가설을 부등식으로 표현 (H0: 귀무가설, H1: 대립가설, μ: 모평균)
    hypotheses = {
        "two-sided": {"H0": f"μ = {popmean}", "H1": f"μ ≠ {popmean}"},
        "less":      {"H0": f"μ ≥ {popmean}", "H1": f"μ < {popmean}"},
        "greater":   {"H0": f"μ ≤ {popmean}", "H1": f"μ > {popmean}"},
    }

    rows = []
    # 양측, 좌측단측, 우측단측을 일괄 검정
    for alt in ("two-sided", "less", "greater"):
        if is_normal:       # 정규성 충족 -> 일표본 t검정
            stat, p = ttest_1samp(sample[column], popmean, alternative=alt)
        else:
            stat, p = wilcoxon(sample[column] - popmean, alternative=alt)

        # p < alpha 이면 통계적으로 유의 (귀무가설 기각)
        significant = p < alpha

        rows.append({
            "test": test_name,
            "alternative": alt,
            "statistic": round(float(stat), 4),
            "p-value": round(float(p), 4),
            "significant": significant,
            # 유의하면 대립가설(H1) 채택, 아니면 귀무가설(H0) 유지
            "result": hypotheses[alt]["H1"] if significant else hypotheses[alt]["H0"],
        })

    # 세 방향 결과를 표로 정리하여 반환
    return DataFrame(rows).set_index(["test", "alternative"])