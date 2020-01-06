# Python期末项目

- 该仓库为中大南方18级Python课程期末项目。该项目与17级学长合作共同完成

### 项目过程：利用python爬取数据，收集故事所需信息—>运用flask框架实现Python和HTML图表前后端各项交互，在web页面展现数据图表和并描述故事—>实现pythonanywhere部署及github上传

### 从国家GDP与工业排放来探究空气污染与两者得相关性
#### 网站内容通过使用Python完成数据处理、数据可视化，并部署于PythonAnywhere上展示。
# 网站一共含有为9个页面
[项目代码GitHub_URL](https://github.com/Tengzyi/qmxm_Python)

[PythonAnywhere个人部署URL](tzyi.pythonanywhere.com)
tzyi.pythonanywhere.com（链接可能有问题）
#### 数据传输描述：
* 利用函数pd.read_csv，读取csv文件
* 利用return render_template跳转页面
* 前后端传输

  request.form["the_region_selected"]
  
  {% for item in the_select_region %}
  
  {{ the_plot_all|safe }}
  
  {{ the_res|safe }}
#### HTML档描述：
* 布局与样式：
1. 标题文字居中，背景为渐变色。
2. 插入轮播图（详见summary.html）。
* 与python文档的数据交互：
1. 与py文件进行对应可视化表格传输（详见hurun.html），通过 <option value="{{ item }}">{{ item }}创建下拉框和通过<input value='Do it!' type='SUBMIT'>设置跳转按钮实现页面跳转；创建HTML控件按钮，举一个代码例子：<p><input value='下一页：地区空气污染浓度' type='SUBMIT'></p >。
2. 数据循环与嵌套：{% for item in the_select_region %}用for循环选择app.py里一个函数的变量里的国家。
* jinja2的运用：
1. <title>{{ the_title }}</title>(来自空气污染导致的死亡率.html）
2. {{ the_plot_all|safe }}（来自hurun.html）。
* 链接css：*<link rel="stylesheet" href="static/css.css"/>*（来自空气污染导致的死亡率.html）。 

#### Python档描述：
* 调用函数
* 新建函数
* 读取csv数据文件 
* 通过post方法实现与前端html页面跳转
* df1.to_html() 实现表格页面  
* request.form["the_region_selected"]获取用户输入

#### Web APP动作档描述：
* 下拉框：在hurun.html文件中，我们设置了发达国家的工业碳氧化物排放下拉框选择，通过点击“Do it”提交，网页即呈现对应国家的排放数据图表：
* 下一页按钮： 在html文件中，我们的故事是通过几个方面阐述的，一个表现为一个界面，通过点击下一页按钮即可跳转至下一个分析。
