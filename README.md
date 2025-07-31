# pi5-ads1115-tools

该仓库提供在树莓派 Pi5 上使用 ADS1115 模数转换器的示例代码和简单说明。

示例设备图片：
<img src="device.jpg" alt="Device" width="300" />

## 环境准备

1. 在 `raspi-config` 中启用 I2C，并重启系统。
2. 安装 Python 相关依赖：

```bash
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y
```

## 创建虚拟环境并安装库

```bash
python3 -m venv venv
source venv/bin/activate
pip install adafruit-circuitpython-ads1x15 adafruit-blinka lgpio
```
## 接线说明

- ADS1115 VCC 接 Raspberry Pi 3.3V
- ADS1115 GND 接 Raspberry Pi GND
- ADS1115 SCL 接 Raspberry Pi PIN 5 (BCM 3)
- ADS1115 SDA 接 Raspberry Pi PIN 3 (BCM 2)

代码使用 `board.SCL` 与 `board.SDA`，在 Pi5 上无需额外适配，只要启用 I2C 即可。

## 查找 I2C 总线和地址

Pi5 可能暴露多路 I2C 接口，可以先列出系统检测到的总线：

```bash
i2cdetect -l
```

示例输出：

```
i2c-1   i2c        Synopsys DesignWare I2C adapter  I2C adapter
i2c-10  i2c        Synopsys DesignWare I2C adapter  I2C adapter
i2c-13  i2c        107d508200.i2c                   I2C adapter
i2c-14  i2c        107d508280.i2c                   I2C adapter
```

接着依次对各个编号执行 `i2cdetect`，能扫到 `0x48` 即为 ADS1115 所在总线：

```bash
sudo i2cdetect -y 1
sudo i2cdetect -y 10
sudo i2cdetect -y 13
sudo i2cdetect -y 14
```

确定好总线与地址后，可在代码中指定：

```python
i2c = busio.I2C(board.SCL, board.SDA)  # 可按需要更换 busnum
ads = ADS.ADS1115(i2c, address=0x48)
```


## 运行示例

示例分为 `main.py` 和 `ads_reader.py` 两个文件。`main.py` 通过 `--pin` 参数指定读取的 ADS1115 通道（0~3），并调用 `ads_reader.py` 中的功能持续打印电压值：

```bash
source venv/bin/activate
python main.py --pin 0
```

脚本运行后每秒打印一次所选通道的电压值和原始数值。

## 简单测试方法

可以将选定的 ADS1115 输入脚接到 3.3V (VCC) 或接地 (GND)
，然后运行脚本，即可观察到电压读数分别接近 3.3V 或 0V，用于验证连线和库安装是否正确。
