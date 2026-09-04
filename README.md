<div align="center">

# VidMuse Video Creator

### 对 Agent 说一句话，从首次授权走到图片、视频与 B-roll 成品

[English](README.en.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

<a href="https://vidmuse.ai/"><img src="docs/images/vidmuse-official-logo.svg" alt="VidMuse" width="240" /></a>

[![Skill](https://img.shields.io/badge/Agent-Skill-7C3AED)](skills/vidmuse-video-creator/SKILL.md)
[![Validate](https://github.com/erduo1998-cell/vidmuse-video-creator/actions/workflows/validate.yml/badge.svg)](https://github.com/erduo1998-cell/vidmuse-video-creator/actions/workflows/validate.yml)
[![VidMuse](https://img.shields.io/badge/Powered%20by-VidMuse-06B6D4)](https://vidmuse.ai/)
[![License](https://img.shields.io/badge/License-MIT-22C55E)](LICENSE)

**由耳总开发与维护 · 获 VidMuse 合作与赞助支持**

[注册 / 登录 VidMuse](https://vidmuse.ai/login) · [官方 CLI](https://vidmuse.ai/en/cli) · [查看当前套餐](https://vidmuse.ai/en/pricing)

</div>

## 合作伙伴：VidMuse

[![VidMuse AI 产品广告平台主视觉](docs/images/vidmuse-product-ads-official.jpg)](https://vidmuse.ai/)

特别感谢 **[VidMuse](https://vidmuse.ai/)** 对本开源 Skill 的合作与赞助支持。VidMuse 提供平台注册、官方 CLI、云端模型与生成服务；本仓库负责把这些能力整理成 Agent 可以直接操作、可恢复、可交付的工作流。

> 上方 Logo 与平台主视觉来自 VidMuse 官方网站，版权与商标归 VidMuse Team / SandAI；仅用于展示合作关系与介绍赞助平台，不属于本仓库 MIT 开源素材。

![VidMuse Video Creator workflow](docs/images/vidmuse-creator-flow.png)

## 它解决什么

用户安装 Skill 后，只需完成一次 VidMuse 注册与授权。此后可以直接让 Agent：

- 查询实时图片、视频、音频、风格和声音模型；
- 按目标、规格和积分筛选模型；
- 文生图、文生视频、图生视频、参考视频和音频驱动生成；
- 把完整 SRT 拆成能解释口播的连续 B-roll；
- 保存任务 ID、追踪到终态、下载文件并留下交付记录；
- 遇到超时或失败时恢复原任务，避免重复提交和重复扣费。

仓库不包含 VidMuse 服务器或 CLI 源码，也不会保存你的账号凭证。平台能力由 [VidMuse](https://vidmuse.ai/) 提供，本仓库负责让 Agent 正确、完整地调用它。

## 真实输出演示

下面是本工作流通过 VidMuse + MiniMax H3 生成，并从原始结果制作 4K 交付版的真实片段：

![VidMuse H3 generated B-roll demo](docs/images/vidmuse-h3-demo.gif)

[下载 4096×3072 的 4K 交付示例](docs/demos/vidmuse-h3-4k-demo.mp4) · [静态预览](docs/images/vidmuse-h3-demo-poster.jpg) · [查看素材说明](docs/demos/README.md)

> 演示证明工作流曾真实跑通，不代表每个模型、提示词或账号都得到相同画面。模型、价格和套餐会变化，Skill 会在生成前查询实时结果。

## 30 秒安装

同时安装到 Codex 和 Claude Code：

```bash
npx skills add erduo1998-cell/vidmuse-video-creator \
  --skill vidmuse-video-creator \
  -g -a codex -a claude-code --copy -y
```

只安装到其中一个 Agent 时，删除不需要的 `-a` 参数。也可以先查看仓库内的 Skill：

```bash
npx skills add erduo1998-cell/vidmuse-video-creator --list
```

## 小白第一次运行

安装后直接对 Agent 说：

```text
使用 $vidmuse-video-creator 帮我完成第一次设置，只做零积分检查，不要生成付费内容。
```

Agent 会完成：

1. 检查并安装 VidMuse 官方 CLI；
2. 打开 [VidMuse 注册 / 登录入口](https://vidmuse.ai/login)；
3. 让你在浏览器或设备页面完成一次授权；
4. 检查账号、套餐以及图片和视频模型是否可用；
5. 不花积分地给出“已就绪”或明确的下一步。

授权后，登录会话保存在你自己的电脑上。Skill、项目目录和 Git 都不接触或上传登录凭证。

## 直接使用

生成图片：

```text
使用 $vidmuse-video-creator 生成一张 16:9 的电影感产品主视觉。
先比较三个可用图片模型和预计积分，我选定后再生成。
```

生成视频：

```text
使用 $vidmuse-video-creator 把 product.png 做成 6 秒 16:9 产品广告。
预算不超过 60 积分，直接追踪到成功并把成片下载到当前项目。
```

制作口播 B-roll：

```text
使用 $vidmuse-video-creator 读取 talk.srt。
先理解全篇，再挑真正需要画面解释的段落，生成连续 B-roll 并交付独立片段。
```

恢复旧任务：

```text
使用 $vidmuse-video-creator 恢复 .vidmuse-work/product-demo，
先查询原任务，不要重新付费提交。
```

## 首次运行验收标准

零积分准备完成必须同时满足：

- CLI 可以运行；
- VidMuse 登录有效；
- 套餐查询成功；
- 实时图片或视频模型列表非空。

首次成片完成还必须满足：平台任务终态成功、文件已下载、文件非空且能打开、交付记录仍如实标注人工审片状态。只有任务 ID 不算完成。

## 安全与隐私

- 凭证只存在 VidMuse CLI 的用户级会话中，不写入仓库。
- `.vidmuse-work/`、输入素材、生成结果和真实项目绑定默认不提交 Git。
- 付费请求先锁定模型、参数、数量和预计积分。
- 已有任务 ID 时只查询原任务，不因轮询慢而重复生成。
- 只上传你有权使用的图片、视频、音乐、声音和人物素材。

详细规则见 [Skill 入口](skills/vidmuse-video-creator/SKILL.md) 与 [首次运行指南](skills/vidmuse-video-creator/references/first-run.md)。

## 品牌与服务边界

VidMuse 商业服务、官方 CLI、品牌和商标由 VidMuse Team / SandAI 维护。本仓库不是 VidMuse 官方 CLI 源码仓库，也不冒充 VidMuse 官方支持渠道。

## 联系耳总

关于 Skill 共建、视频生成工作流、开源合作或商业项目，可以扫码添加耳总微信。此二维码是耳总个人商务联系入口，不是 VidMuse 官方客服：

<img src="docs/images/wechat-qrcode.jpg" alt="耳总微信二维码" width="360" />

## 开发与验证

```bash
python3 tests/validate_repo.py
```

仓库自检不读取 VidMuse 账号，也不会提交生成任务。

## 许可与归属

Skill、脚本和原创文档以 [MIT License](LICENSE) 开源。VidMuse 名称、服务、CLI 与相关品牌资产不在 MIT 授权范围内；演示媒体和微信二维码的归属与使用边界见 [NOTICE.md](NOTICE.md)。
