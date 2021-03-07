# Web构建与测试

本项目的Web端基于Nginx+uWSGI+Flask构建，服务器环境为Centos7.3的云服务器，采用前后端分离的方式进行开发， Web端使用了Vue2.0+Axios+Element UI进行构建与交互。项目主要内容包括用户上传引导、服务端数据处理与结果返回。

### 1. 前端测试部分

#### a. 页面构建

在Element UI库中使用了卡片式模组进行设计，主要包括项目名称、流水单上传部分、企业账单上传部、提交组件与结果返回页面等，使用组件包括el-card，el-button，el-upload等，为了保证响应速度以CDN形式引入源文件。

#### b. 文件上传

文件上传使用Element UI的el-upload模组，以multipart/form-data形式上传文件，并将上传文件格式限制为xls或者xlsx文件格式，限制不允许文件多选，最大文件数量为1个。上传成功后，触发框架中successHandleBank的方法修改上传状态，使得组件响应式渲染为“已经上传”样式。

```php+HTML
<el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>第一步：上传“银行流水单”(仅支持.xls .xlsx格式)</span>
                <el-button style="float: right; padding: 3px 0" type="text">上海科技大学 D.H 队</el-button>
            </div>
            <el-upload class="upload-demo" drag :on-success="successHandleBank" accept=".xls,.xlsx,.xlsm" :limit="1" :multiple="false"  action="http://xxx/uploadBank">
                <i class="el-icon-upload" v-if="!bankOk"></i>
                <i class="el-icon-check" v-if="bankOk"></i>
                <div class="el-upload__text" v-if="!bankOk">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__text" v-if="bankOk">文件已经上传</div>
            </el-upload>
        </el-card>
```

#### c. 文件验证

需要上传的文件POST到服务器对应路径后，触发成功上传回调修改组件状态，当按下底部的“确认提交”按钮时，触发submit函数检测是否两个文件都已经上传，若有错误则调用$notify.error模组进行错误提示，否则触发计算命令，触发云端服务器开始计算。

```javascript
submit(){
            if (!(this.bankOk && this.companyOk)){
                this.$notify.error({
                    title: '错误',
                    message: '请确保两个文件都已经上传'
                });
                return
            }
            this.loading = true
    		 axios.get('http://xxx/submit',{ ....
            },
                
```

### 2.后端测试部分

#### a. 服务端构建

服务端使用了阿里云的轻量应用服务器，安装系统为Centos7.3，配置环境为Nginx+uWSGI+Flask，Nginx被配置为代理本地uWSGI所执行端口，由Flask这一python 轻量级Web框架负责请求处理。

#### b. 服务接口

进入'/upload'路径后将触发upload_file函数按照index.html格式进行渲染，并没有完全采用MVC模型，而是将前端逻辑打包在前端的js文件中进行处理。同时，开启/uploadBank作为文件上传POST的位置，将上传文件存储到对应的文件存储目录下, 在文件上传完成后调用process函数进行处理。处理完成后，对于前端的结果查询接口回复，使前端跳转到结果显示页面。

```python
@app.route('/upload')
def upload_file():
   return render_template('index.html')
   
@app.route('/uploadBank', methods = ['GET', 'POST'])
def uploadBank():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename('xxxx.xls')))
      process('./upload/'+f.filename)
      return "succcess upload"
```

