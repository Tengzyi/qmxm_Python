from flask import Flask, render_template, request
import plotly as py
import cufflinks as cf
from pyecharts.charts import Map, Timeline
from pyecharts import options as opts
import pandas as pd

app = Flask(__name__)

df1 = pd.read_csv("Industrial_emission_index.csv", encoding='utf-8')
df2 = pd.read_csv("Death_rates_from_air_pollution.csv", encoding='utf-8')

regions_available = list(df1.country.dropna().unique())


def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2007, 2017):
        map0 = (
            Map()
                .add(
                "", list(zip(list(df2.Country), list(df2["{}年".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="2007年-2017年各地区GDP对比".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(max_=21972347748529, min_=20439158.42),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl


timeline_map().render()


@app.route('/')
def bing_death():
    return render_template('2017年死亡因素下的死亡人数比例对比.html',
                           the_title='2017年死亡因素下的死亡人数比例对比')


@app.route('/2', methods=['POST'])
def zhexian_death():
    return render_template('空气污染死亡人数对比折线图.html',
                           the_title='空气污染死亡人数对比折线图')


@app.route('/3', methods=['POST'])
def map_gdp():
    return render_template('2007年-2017年各地区GDP对比.html',
                           the_title='2007年-2017年各地区GDP对比')


@app.route('/4', methods=['POST'])
def map_death():
    return render_template('2007年-2017年空气污染导致的死亡率.html',
                           the_title='2007年-2017年空气污染导致的死亡率')


@app.route('/5', methods=['POST'])
def map_air():
    return render_template('地区空气污染浓度.html',
                           the_title='地区空气污染浓度')


@app.route('/6', methods=['POST'])
def zhuzhaung_mm():
    return render_template('min&max.html',
                           the_title='min&max')


@app.route('/7', methods=['POST'])
def xian_pollution():
    data_str = df1.to_html()
    return render_template('hurun.html',
                           the_title='发达国家工业污染物排放量',
                           the_res=data_str,
                           the_select_region=regions_available
                           )


@app.route('/hurun', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="发达国家工业污染物排放量.html", auto_open=False)
    with open("发达国家工业污染物排放量.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()

    return render_template('hurun.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )


@app.route('/summary', methods=['POST'])
def summary():
    return render_template('summary.html',
                           the_title='总结')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=8080)
