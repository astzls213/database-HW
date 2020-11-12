# database-HW
暨南大学数据库系统概念实验课项目

### Preparing

1. 请确保已安装MySQL，现在先做下面的工作：

   ```sql
   # 登录MySQL
   $ mysql -u root -p
   # 创建账户
   create user dev identified by 'usefordev';
   create user dbhw identified by 'iamp@$$wd';
   # 创建数据库
   create database dev_db;
   create database hw_db;
   # 分配权限
   grant all on dev_db.* to dev;
   grant all on hw_db.* to dbhw;
   ```

2. 

### Install



### Demo