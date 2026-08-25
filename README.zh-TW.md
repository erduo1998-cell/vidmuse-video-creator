<div align="center">

# VidMuse Video Creator

### 一次授權，讓 Agent 直接交付圖片、影片與 B-roll

[简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

[註冊 / 登入 VidMuse](https://vidmuse.ai/login) · [官方 CLI](https://vidmuse.ai/zh-TW/cli)

</div>

![VidMuse Video Creator workflow](docs/images/vidmuse-creator-flow.png)

本 Skill 會安裝並操作 VidMuse 官方 CLI。使用者完成一次瀏覽器或裝置授權後，Agent 就能查詢即時模型與點數、生成圖片或影片、製作 SRT B-roll、追蹤非同步任務、下載成品並留下交付紀錄。

## 安裝

```bash
npx skills add erduo1998-cell/vidmuse-video-creator \
  --skill vidmuse-video-creator \
  -g -a codex -a claude-code --copy -y
```

## 第一次執行

```text
使用 $vidmuse-video-creator 完成首次設定，只做零點數檢查，不要提交付費生成。
```

準備完成必須同時確認：CLI 可執行、登入有效、方案查詢成功、即時圖片或影片模型清單非空。登入憑證只留在使用者自己的 CLI 會話，不會寫入專案或 Git。

## 真實輸出

![VidMuse H3 generated B-roll demo](docs/images/vidmuse-h3-demo.gif)

[下載 4096×3072 的 4K 交付示例](docs/demos/vidmuse-h3-4k-demo.mp4) · [靜態預覽](docs/images/vidmuse-h3-demo-poster.jpg) · [媒體說明](docs/demos/README.md)

本專案由耳總開發維護，獲 VidMuse 合作與贊助支持。VidMuse 商業服務、官方 CLI、名稱與商標由 VidMuse Team / SandAI 維護；本倉庫不包含官方服務或 CLI 原始碼，也不是官方客服管道。

以下為耳總個人商務聯絡入口，並非 VidMuse 官方客服：

<img src="docs/images/wechat-qrcode.jpg" alt="耳總微信 QR Code" width="360" />

原創 Skill、腳本與文件使用 [MIT License](LICENSE)。商標與媒體說明見 [NOTICE.md](NOTICE.md)。
