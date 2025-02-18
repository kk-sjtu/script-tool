### bash code block
git remote add org <组织仓库的URL>

### bash code block
#!/bin/sh

# 推送到个人仓库
git push origin main

# 推送到组织仓库
git push org main

### bash code block
touch .git/hooks/post-commit

### bash code block
nano .git/hooks/post-commit

### bash code block
#!/bin/sh

echo "正在同步到个人仓库..."
git push origin main

echo "正在同步到组织仓库..."
git push org main

echo "同步完成！"

### bash code block
chmod +x .git/hooks/post-commit

### bash code block
git commit -m "测试提交"

### bash code block
正在同步到个人仓库...
正在同步到组织仓库...
同步完成！

