from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np
from pandas import pivot_table

# ----------------------------------------------------------

def init(width=1280, height=640, rows=1, cols=1,
         title=None, xlabel=None, ylabel=None, grid=True):
    """
    그래프의 크기와 dpi를 설정하여 fig와 ax 객체를 반환하는 함수

    Parameters:
        - width: 그래프의 가로 크기 (픽셀 단위)
        - height: 그래프의 세로 크기 (픽셀 단위)
        - rows: 그래프의 행 수
        - cols: 그래프의 열 수
        - title: 그래프의 제목 (기본값: None)
        - xlabel: x축 레이블 (기본값: None)
        - ylabel: y축 레이블 (기본값: None)
        - grid: 그래프에 그리드를 표시할지 여부 (기본값: True)

    Returns:
        - fig: 생성된 Figure 객체
        - ax: 생성된 Axes 객체 또는 Axes 배열
    """
    my_figsize = (width / 100, height / 100)
    fig, ax = plt.subplots(rows, cols, figsize=my_figsize)
    ax.grid(grid, alpha=0.5)

    if title:
        ax.set_title(title, fontsize=24, fontweight=500, pad=15)

    if xlabel:
        ax.set_xlabel(xlabel, fontsize=16, fontweight=400, labelpad=5)

    if ylabel:
        ax.set_ylabel(ylabel, fontsize=16, fontweight=400, labelpad=5)

    return fig, ax

# ----------------------------------------------------------

def show(save_path=None):
    """
    그래프를 화면에 표시하는 함수

    Parameters:
        - grid: 그리드를 표시할지 여부 (기본값: True)
        - save_path: 그래프를 저장할 파일 경로, None이면 저장하지 않음
    """
    if save_path:
        plt.savefig(save_path)
        
    plt.tight_layout()
    plt.show()
    plt.close()





def lineplot(data=None, x=None, y=None, hue=None,
             title=None, xlabel=None, ylabel=None,
             color=None, linewidth=None, linestyle="-", palette=None,
             marker=None, markersize=None, markeredgewidth=None,
             markeredgecolor=None, markerfacecolor=None,
             width=1280, height=640, save_path=None):
    """
    선 그래프를 그린다.

    Args:
        data: 시각화할 데이터
        x: x축 컬럼명 혹은 x축 값 시퀀스
        y: y축 컬럼명 혹은 y축 값 시퀀스
        hue: 범주 구분 컬럼명
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        color: 선 색상
        linewidth: 선 굵기
        linestyle: 선 스타일
        palette: 색상 팔레트 이름
        marker: 마커 모양
        markersize: 마커 크기
        markeredgewidth: 마커 테두리 두께
        markeredgecolor: 마커 테두리 색상
        markerfacecolor: 마커 배경 색상
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로        
    """

    # 그래프 초기화
    init(width=width, height=height, title=title, xlabel=xlabel, ylabel=ylabel)

    # 선 그래프 그리기
    sb.lineplot(data=data, x=x, y=y, hue=hue,
             color=color, linewidth=linewidth, linestyle=linestyle,
             palette=palette, marker=marker, markersize=markersize,
             markeredgewidth=markeredgewidth,
             markeredgecolor=markeredgecolor,
             markerfacecolor=markerfacecolor)

    # 그래프 표시
    show(save_path=save_path)





def kdeplot(data=None, x=None, hue=None, meanline=False,
            title=None, xlabel=None, ylabel=None,
            fill=False, linewidth=2.0, palette=None,
            width=1280, height=640, save_path=None):

    """
    단변량 커널 밀도 그래프를 그린다. 평균선은 hue가 설정된 경우 지원하지 않는다.

    Args:
        data: 시각화할 데이터
        x: x축 컬럼명 혹은 x축 값 시퀀스
        hue: 범주형 변수 이름 (기본값 None)
        meanline: 평균선 표시 여부
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        fill: 면적 채우기 여부
        linewidth: 선 굵기
        palette: 색상 팔레트 이름
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로 
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title,
                   xlabel=xlabel, ylabel=ylabel)

    # 단변량 커널 밀도 그래프 그리기
    sb.kdeplot(data=data, x=x, hue=hue, fill=fill, linewidth=linewidth,
               palette=palette)

    # 평균선 표시
    if meanline:
        y_max = ax.get_ylim()[1]

        if hue is None:
            mv = data[x].mean()
            ax.axvline(x=mv, color='red', linestyle='--', linewidth=linewidth * 0.5)
            ax.text(x=mv + 0.05, y=y_max * 0.95, s=f'Mean: {mv:.2f}', color='red', fontsize=14,
                    ha='center')
        else:
            # hue 범주별 평균선 표시 (kdeplot이 그린 라인의 색상과 일치시킴)
            categories = list(data[hue].unique())
            # 팔레트에서 범주의 수에 맞는 색상값 추출
            colors = sb.color_palette(palette, n_colors=len(categories))

            # 각 범주에 대해 평균선 표시
            for i, cat in enumerate(categories):
                mv = data.loc[data[hue] == cat, x].mean()
                ax.axvline(x=mv, color=colors[i], linestyle='--', linewidth=linewidth * 0.5)
                ax.text(x=mv + 0.05, y=y_max * (0.95 - i * 0.07), s=f'{cat} Mean: {mv:.2f}',
                        color=colors[i], fontsize=14, ha='center')

    # 출력
    show(save_path=save_path)




def histplot(data=None, x=None, bins=None, hue=None,
            title=None, xlabel=None, ylabel=None,
            linewidth=1, palette=None, kde=False,
            width=1280, height=640, save_path=None):
    """
    히스토그램을 그린다.

    Args:
        data: 시각화할 데이터
        x: 히스토그램 대상 컬럼명
        bins: 구간 수 또는 경계
        hue: 범주 컬럼명
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        linewidth: 선 굵기
        palette: 색상 팔레트 이름
        kde: 커널 밀도 그래프 겹쳐 그릴지 여부
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title, xlabel=xlabel, ylabel=ylabel)

    # 구간 산정
    if isinstance(bins, int):
        hist, bins = np.histogram(data[x], bins=bins)
        bins = np.round(bins, 1)
        ax.set_xticks(bins, bins)
    elif isinstance(bins, (list, np.ndarray)):
        ax.set_xticks(bins, bins)

    # 히스토그램 그리기
    sb.histplot(data=data, x=x, hue=hue, linewidth=linewidth,
                palette=palette, kde=kde, bins=bins)

    # 그래프 표시
    show(save_path=save_path)





def _resolve_hue(cat_axis, hue=None, palette=None):
    """
    범주형 그래프(boxplot, violinplot, barplot, countplot)의 hue 관련 인자를 결정한다.

    범주축을 기준으로 다음 두 경우를 처리한다.
        - hue 없이 palette만 지정: 범주축을 hue로 삼아 범주별 색상을 적용
        - hue가 범주축과 동일(중복): 외부에서 hue=x 로 호출된 경우
    두 경우 모두 hue가 범주축과 같으므로, 그래프가 쪼개지지(dodge) 않게 끄고 범례도 숨긴다.

    Args:
        cat_axis: 범주축 컬럼명 (세로형이면 x, 가로형이면 y)
        hue: 범주 구분 컬럼명
        palette: 색상 팔레트 이름

    Returns:
        - hue: seaborn에 전달할 hue 값
        - dodge: seaborn에 전달할 dodge 값
        - legend: seaborn에 전달할 legend 값
    """
    if hue is None and palette is not None:
        return cat_axis, False, False

    if hue is not None and hue == cat_axis:
        return hue, False, False

    return hue, "auto", "auto"





def boxplot(data=None, x=None, y=None, hue=None, orient=None, palette=None,
            order=None, title=None, xlabel=None, ylabel=None,
            width=1280, height=640, save_path=None):
    """
    상자그림(boxplot)을 그린다.

    Args:
        data: 시각화할 데이터
        x: x축 범주 컬럼명
        y: y축 값 컬럼명
        hue: 범주 구분 컬럼명
        orient: 상자그림 방향 (None, 'v' 또는 'h')
        palette: 색상 팔레트 이름
        order: 상자그림 순서를 의미하는 연속형 자료형
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title, xlabel=xlabel, ylabel=ylabel)

    # 범주축과 hue가 겹치는 경우 상자가 쪼개지지(dodge) 않도록 처리
    hue, dodge, legend = _resolve_hue(x if orient !="h" else y,
                                      hue=hue, palette=palette)

    # 상자그림 그리기
    sb.boxplot(data=data, x=x, y=y, hue=hue, orient=orient,
               palette=palette, order=order, dodge=dodge, legend=legend)

    # 그래프 표시
    show(save_path=save_path)





def violinplot(data=None, x=None, y=None, hue=None, orient=None,
               palette=None, title=None, xlabel=None, ylabel=None,
               width=1280, height=640, save_path=None):
    """
    바이올린 플롯(ViolinPlot)을 그린다.

    Args:
        data: 시각화할 데이터
        x: x축 범주 컬럼명
        y: y축 값 컬럼명
        hue: 범주 구분 컬럼명
        orient: 바이올린 플롯 방향 (None, 'v' 또는 'h')
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title, xlabel=xlabel,
                   ylabel=ylabel)

    # 범주축과 hue가 겹치는 경우 상자가 쪼개지지(dodge) 않도록 처리
    hue, dodge, legend = _resolve_hue(x if orient !="h" else y,
                                      hue=hue, palette=palette)

    # 바이올린 플롯 그리기
    sb.violinplot(data=data, x=x, y=y, hue=hue, orient=orient,
               palette=palette, dodge=dodge, legend=legend)

    # 그래프 표시
    show(save_path=save_path)





def heatmap(data=None, annot=True, fmt="0.2f", linewidth=0.5,
            palette=None, title=None, xlabel=None, ylabel=None,
            width=1280, height=640, save_path=None):
    """
    히트맵을 그린다.

    Args:
        data: 시각화할 데이터 (2차원 배열 또는 DataFrame)
        annot: 셀에 값 표시 여부
        fmt: 셀에 표시할 값의 형식
        linwidth: 셀 간격 선 두께
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title, xlabel=xlabel,
                   ylabel=ylabel)

    # 그리드 제거
    ax.grid(False)

    # 히트맵 그리기
    sb.heatmap(data=data, annot=annot, fmt=fmt, linewidth=linewidth,
               cmap=palette)

    # 그래프 표시
    show(save_path=save_path)





def barplot(data=None, x=None, y=None, hue=None, estimator=np.mean,
            order=None, palette=None, title=None, xlabel=None, ylabel=None,
            width=1280, height=640, save_path=None):
    """
    막대그래프를 그린다.

    Args:
        data: 시각화할 데이터 (2차원 배열 또는 DataFrame)
        x: x축 범주 컬럼명
        y: y축 값 컬럼명
        hue: 범주 구분 컬럼명
        estimator: 막대 높이 계산 함수 (기본값: np.mean)
        order: 정렬순서를 의미하는 연속형 자료형
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height,
                   title=title, xlabel=xlabel, ylabel=ylabel)

    # 범주축과 hue가 겹치는 경우 상자가 쪼개지지(dodge) 않도록 처리
    hue, dodge, legend = _resolve_hue(x if x is not None else y, hue=hue,
                                      palette=palette)

    # 막대그래프 그리기
    sb.barplot(data=data, x=x, y=y, hue=hue, estimator=estimator,
               order=order, palette=palette, dodge=dodge, legend=legend)

    # 그래프 표시
    show(save_path=save_path)





def countplot(data=None, x=None, y=None, hue=None, order=None,
              palette=None, title=None, xlabel=None, ylabel=None,
              width=1280, height=640, save_path=None):
    """
    막대그래프를 그린다.

    Args:
        data: 시각화할 데이터 (2차원 배열 또는 DataFrame)
        x: x축 범주 컬럼명
        y: y축 값 컬럼명
        hue: 범주 구분 컬럼명
        order: 정렬순서를 의미하는 연속형 자료형
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height,
                   title=title, xlabel=xlabel, ylabel=ylabel)

    # 범주축과 hue가 겹치는 경우 상자가 쪼개지지(dodge) 않도록 처리
    hue, dodge, legend = _resolve_hue(x if x is not None else y, hue=hue,
                                      palette=palette)

    # 빈도 그래프 그리기
    sb.countplot(data=data, x=x, y=y, hue=hue, order=order,
                 palette=palette, dodge=dodge, legend=legend)

    # 그래프 표시
    show(save_path=save_path)





def pieplot(x, labels, autopct='%.1f%%', startangle=90, counterclock=False,
            explode=None, donutchart=False,
            wedge_width=0.7, wedge_color='#ffffff', wedge_linewidth=3,
            palette=None, title=None, xlabel=None, ylabel=None,
            width=1280, height=640, save_path=None):
    """
    파이 그래프 혹은 도넛 그래프를 그린다.

    Args:
        x: x축 범주 컬럼명
        labels: 파이 조각에 대한 라벨
        autopct: 퍼센트 표시 형식
        startangle: 시작 각도
        counterclock: 시계 반대 방향으로 그릴지 여부
        explode: 조각 간격
        donutchart: 도넛 차트 여부
        wedge_width: 도넛 차트일 때 조각 너비 비율
        wedge_color: 도넛 차트일 때 조각 사이 경계선 색상
        wedge_linewidth: 도넛 차트일 때 조각 사이 경계선 굵기
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title,
                   xlabel=xlabel, ylabel=ylabel)

    # 색상값을 팔레트로부터 추출
    color_list = None
    if palette:
        color_list = sb.color_palette(palette, n_colors=len(labels))

    # 도넛 그래프 그리기 옵션 생성
    wedgeprops = None
    if donutchart:
        wedgeprops={'width': wedge_width, 'edgecolor': wedge_color, 'linewidth': wedge_linewidth}

    # 파이 그래프 그리기
    ax.pie(x, labels=labels, autopct=autopct, startangle=startangle,
           counterclock=counterclock, explode=explode,
           colors=color_list, wedgeprops=wedgeprops)

    # 그래프 표시
    show(save_path=save_path)





def stackplot(data, x, y, hue, aggfunc=np.sum, orient='v', ratio=False,
              text=True, text_color="#ffffff", text_fontsize=12,
              text_format=None,
              palette=None, title=None, xlabel=None, ylabel=None,
              width=1280, height=640, save_path=None):
    """
    누적 막대 그래프를 그린다.

    Args:
        data: 시각화할 데이터
        x: x축 범주 컬럼명
        y: y축 값 컬럼명
        hue: 범주 구분 컬럼명
        aggfunc: 누적할 값 계산 함수 (기본값: np.sum)
        orient: 막대 방향 ('v' 또는 'h')
        ratio: 누적값을 비율로 표시할지 여부
        text: 누적값 텍스트 표시 여부
        text_color: 누적값 텍스트 색상
        text_fontsize: 누적값 텍스트 폰트 크기
        text_format: 누적값 텍스트 포맷
        palette: 색상 팔레트 이름
        title: 그래프 제목
        xlabel: x축 레이블
        ylabel: y축 레이블
        width: 캔버스 가로 픽셀
        height: 캔버스 세로 픽셀
        save_path: 이미지 저장 경로
    """
    # 그래프 초기화
    fig, ax = init(width=width, height=height, title=title,
                   xlabel=xlabel, ylabel=ylabel)

    # 데이터 피버팅
    df = pivot_table(data=data, index=x, values=y, columns=hue, aggfunc=aggfunc,
                     fill_value=0, observed=True)
    df.index = df.index.astype("str").astype("category")

    # 누적값을 비율로 변환하는 경우
    if ratio:
        if text_format is None:         # 텍스트 포맷이 없다면 강제 지정
            text_format = "{:.1f}%"

        df['sum'] = df.sum(axis=1)      # 각 행의 합을 계산해 'sum'열에 저장

        for col in df.columns:          # 각 열에 대해 누적값을 비율로 변환
            df[col] = df[col] / df['sum'] * 100

        df.drop('sum', axis=1, inplace=True)    # 'sum' 열 제거

        if orient == 'v':               # 그래프 방향에 따라 축 범위 설정
            ax.set_ylim(0, 100)
        else:
            ax.set_xlim(0, 100)

    else:
        if text_format is None:         # 텍스트 포맷이 없다면 강제 지정
            text_format = "{:.1f}"

    # 색상값 생성하기
    color_list = None
    if palette is not None:
        color_list = sb.color_palette(palette, n_colors=len(df.columns))

    # 피벗테이블의 각 열에 대해 누적 막대그래프 그리기
    for i, col in enumerate(df.columns):
        color = None

        if color_list is not None:
            color = color_list[i]

        if orient == 'y':
            ax.bar(df.index, df[col], bottom=df.iloc[:, :i].sum(axis=1), color=color,
                   label=col)
        else:
            ax.barh(df.index, df[col], left=df.iloc[:, :i].sum(axis=1), color=color,
                   label=col)

    # 누적값 텍스트 표시
        if text:
            for j, val in enumerate(df[col]):
                if val == 0: # 누적값이 0인 경우 텍스트 표시하지 않음
                    continue

                if orient == 'v':
                    ax.text(x=j, y=df.iloc[j, :i].sum() + val / 2,
                            s=text_format.format(val), ha='center', va='center',
                            color=text_color, fontsize=text_fontsize)

                else:
                    ax.text(x=df.iloc[j, :i].sum() + val / 2, y=j,
                            s=text_format.format(val), ha='center', va='center',
                            color=text_color, fontsize=text_fontsize)

    # 범례 표시
    ax.legend(bbox_to_anchor=(1, 1))

    # 그래프 표시
    show(save_path=save_path)