<div align="center">

# VidMuse Video Creator

### 한 번의 인증으로 이미지·영상·B-roll 완성본까지 Agent가 실행

[简体中文](README.md) · [English](README.en.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md)

<a href="https://vidmuse.ai/"><img src="docs/images/vidmuse-official-logo.svg" alt="VidMuse" width="240" /></a>

[VidMuse 가입 / 로그인](https://vidmuse.ai/login) · [공식 CLI](https://vidmuse.ai/en/cli)

</div>

## 파트너 및 후원사: VidMuse

[![VidMuse AI 제품 광고 플랫폼 메인 비주얼](docs/images/vidmuse-product-ads-official.jpg)](https://vidmuse.ai/)

이 오픈소스 Skill의 협업과 후원을 지원한 **[VidMuse](https://vidmuse.ai/)** 에 특별히 감사드립니다. VidMuse는 계정, 공식 CLI, 클라우드 모델과 생성 서비스를 제공하고, 이 저장소는 그 기능을 Agent가 직접 실행하고 재개하여 결과물까지 납품할 수 있는 워크플로로 정리합니다.

> 위 Logo와 플랫폼 이미지는 VidMuse 공식 웹사이트에서 가져왔습니다. 저작권과 상표는 VidMuse Team / SandAI에 있으며 이 저장소의 MIT License에 포함되지 않습니다.

![VidMuse Video Creator workflow](docs/images/vidmuse-creator-flow.png)

이 Agent Skill은 VidMuse 공식 CLI를 설치하고 작동합니다. 브라우저 또는 기기에서 한 번 인증한 뒤에는 Agent가 실시간 모델과 크레딧을 확인하고, 이미지와 영상을 생성하며, SRT 기반 B-roll 제작·비동기 작업 추적·다운로드·납품 기록까지 처리할 수 있습니다.

## 설치

```bash
npx skills add erduo1998-cell/vidmuse-video-creator \
  --skill vidmuse-video-creator \
  -g -a codex -a claude-code --copy -y
```

## 첫 실행

```text
$vidmuse-video-creator를 사용해 최초 설정을 완료하세요.
크레딧이 들지 않는 준비 검사만 하고 유료 생성은 제출하지 마세요.
```

CLI 실행, 유효한 로그인, 요금제 조회, 비어 있지 않은 실시간 이미지 또는 영상 모델 목록이 모두 확인되어야 준비 완료입니다. 인증 정보는 사용자의 CLI 세션에만 저장되며 프로젝트나 Git에 기록되지 않습니다.

## 실제 생성 예시

![VidMuse H3 generated B-roll demo](docs/images/vidmuse-h3-demo.gif)

[4096×3072 납품 예시 다운로드](docs/demos/vidmuse-h3-4k-demo.mp4) · [정적 미리보기](docs/images/vidmuse-h3-demo-poster.jpg) · [미디어 설명](docs/demos/README.md)

## 브랜드 및 서비스 범위

VidMuse 상용 서비스, 공식 CLI, 이름과 상표는 VidMuse Team / SandAI가 관리합니다. 이 저장소는 공식 CLI 소스나 공식 지원 채널이 아닙니다.

Skill 협업, 영상 워크플로 또는 상업 프로젝트 문의는 Erduo 개인 비즈니스 WeChat으로 연락할 수 있습니다. VidMuse 공식 고객 지원 채널이 아닙니다.

<img src="docs/images/wechat-qrcode.jpg" alt="Erduo WeChat QR code" width="360" />

원본 Skill, 스크립트와 문서는 [MIT License](LICENSE)로 공개됩니다. 상표와 미디어 정보는 [NOTICE.md](NOTICE.md)를 확인하세요.
