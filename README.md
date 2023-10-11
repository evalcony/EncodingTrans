# 文件编码转换

自动对文件的编码进行识别，并将不同编码的文件统一转换为同一编码。

首先执行 init.sh 文件初始化，在桌面创建 py-encoding-input, py-encoding-output 文件。然后将需要转换编码的文件放入 py-encoding-input 中。 

执行命令，即可完成文件编码转换。例如这里将 `.tra` 文件转换为 `utf-8` 编码。

```
python3 main.py -type .tra -to utf-8
```