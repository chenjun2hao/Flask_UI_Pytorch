# Flask简单UI做深度学习展示用
**简介：**python flask能很快的做一个web应用，同时，深度学习展示的在终端中用命令行的方式进行结果展示是很不友好的方式，所以最好是做一个简单的web，简单的提交图片，预览图片，显示结果。这篇博客就从这样的目标出发。这里可以参考pytorch官方的[一个教程](https://github.com/avinassh/pytorch-flask-api-heroku)，但是这个教程没有提交图像的预览和结果图片的显示。

## 关键流程
    1. 提交测试图像和附加字符串信息
    2. 测试图像预览
    3. 结果图像显示
整个不涉及html和java语法介绍

## 1. 提交测试图像和附加字符串信息
```python
测试图像
    - python端
        f = request.files['file']
        file = request.files.get('file')
    - html端
        <form class="form-signin" method=post enctype=multipart/form-data>
            <input type="file" name="file" class="form-control-file" id="inputfile">
        </form>
        关键就是form要声明method为posd，enctype为mutipart/form-data
        input的name对应python端的request.files['file']
获得字符串：
    - python端
        user_input = request.form.get("name")
        利用的是request的form属性

    - html端
        <form action="" enctype='multipart/form-data' method='POST'>
            <input type="text" class="txt_input" name="name"  value="超超开心" style="margin-top:10px;"/>
        </form>
```
## 2. 上传的时候图片预览：
利用的是javascript的脚本：

    // 用javascript进行上传图片的可视化
    let fileObj = this.files[0];
    // 生成一个文件读取的内置对象
    let fileReader = new FileReader();
    // 将文件对象传递给内置对象
    fileReader.readAsDataURL(fileObj); //这是一个异步执行的过程，所以需要onload回调函数执行读取数据后的操作
    // 将读取出文件对象替换到img标签
    fileReader.onload = function(){  // 等待文件阅读器读取完毕再渲染图片
    $('#myfile').attr('src',fileReader.result)
具体可以参考index.html

## 3. 处理结果的展示：
可以采用两种方案：
1. 将pytorch/tensorflow处理之后的结果保存到计算机，显示的时候用html的src标签读取图片
```
    <img src="{{ url_for('static', filename= './images/test.jpg',_t=val1) }}">
```
2. 将处理后的图片作为参数出入html中，然后进行显示



# 参考
1. [Flask上传本地图片并在页面上显示](https://blog.csdn.net/dcrmg/article/details/81987808)