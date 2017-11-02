### 基于Celery的离线定时任务管理项目


#### 启动flower监控:
pip install flower
celery flower --port=5555 --broker=redis://ip:port/db
访问web页面: http://localhost:5555


#### 启动worker和beat:
1. 同时启动beat和worker: command=celery worker -B -A celery_app --loglevel=info --logfile=XXX --autoscale=8,4
   日志输出到控制台: command=celery worker -B -A celery_app --loglevel=info --autoscale=8,4
2. 只启动worker: command=celery worker -A celery_app --loglevel=info --logfile=XXX --autoscale=8,4
3. 只启动beat: command=celery beat -A celery_app


#### requirements.txt说明
生成requirements.txt文件：pip freeze > requirements.txt
安装requirements.txt中的依赖包：pip install -r requirements.txt


注: 4.1.0的版本有timezone不生效的bug, 所以使用4.0.2的版本
pip install celery==4.0.2

