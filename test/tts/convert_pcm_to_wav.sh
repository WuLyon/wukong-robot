#!/bin/bash

# 获取脚本路径
script_dir=$(cd "$(dirname "$0")" && pwd)

# 使用说明
show_help() {
    echo "使用说明："
    echo "  $0 [输入文件路径] [输出文件路径]"
    echo "参数："
    echo "  -help            显示脚本使用说明"
    echo "  [输入文件路径]   指定输入 PCM 文件的完整路径，包含文件名"
    echo "  [输出文件路径]   指定输出 WAV 文件的完整路径，包含文件名"
    echo "示例："
    echo "  $0               使用默认路径 demo.pcm 和 demo.wav"
    echo "  $0 input.pcm     指定输入文件为 input.pcm，输出文件为默认路径 demo.wav"
    echo "  $0 input.pcm output.wav  指定输入文件为 input.pcm，输出文件为 output.wav"
    exit 0
}

# 参数检查：处理 -help
if [ "$1" == "-help" ]; then
    show_help
fi

# 参数数量超出限制时的错误提示
if [ $# -gt 2 ]; then
    echo "错误：参数过多！"
    show_help
fi

# 检查输入参数是否是非法选项
if [[ "$1" == -* && "$1" != "-help" ]]; then
    echo "错误：无效选项 $1"
    show_help
fi

if [[ "$2" == -* ]]; then
    echo "错误：无效选项 $2"
    show_help
fi

# 设置输入和输出文件路径
if [ -n "$1" ]; then
    input_file="$1"
else
    input_file="$script_dir/demo.pcm"
fi

if [ -n "$2" ]; then
    output_file="$2"
else
    output_file="$script_dir/demo.wav"
fi

# 设置PCM文件的参数（根据实际情况进行修改）
sample_rate=16000   # 采样率
channels=1          # 单声道
sample_format="s16le" # 16-bit 小端格式

# 检查输入文件是否存在
if [ ! -f "$input_file" ]; then
    echo "错误：找不到输入文件 $input_file"
    exit 1
fi

# 使用 ffmpeg 转换 PCM 文件为 WAV 格式
ffmpeg -f $sample_format -ar $sample_rate -ac $channels -i "$input_file" "$output_file"

# 检查转换是否成功
if [ $? -eq 0 ]; then
    echo "转换成功！输出文件：$output_file"
else
    echo "转换失败！"
    exit 1
fi
