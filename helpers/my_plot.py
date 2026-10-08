from matplotlib import pyplot as plt
import seaborn as sb

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