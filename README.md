<div align="center">

# GKI KernelSU SUSFS

**自动化构建 GKI 内核 | 集成 KernelSU + SUSFS**

[![KernelSU](https://img.shields.io/badge/KernelSU-Supported-green)](https://kernelsu.org/)
[![SUSFS](https://img.shields.io/badge/SUSFS-Integrated-green)](https://gitlab.com/simonpunk/susfs4ksu)
[![Telegram](https://img.shields.io/static/v1?label=Telegram&message=Channel&color=0088cc)](https://t.me/UnofficialReSukiSUGKI)
[![GitHub Release](https://img.shields.io/github/v/release/coolzyd9107/GKI_KernelSU_SUSFS?style=for-the-badge&logo=android&color=green)](https://github.com/coolzyd9107/GKI_KernelSU_SUSFS/releases)
---

</div>

## ⚠️ 仓库须知 ⚠️

① 本仓库分叉自 [zzh20188/GKI_KernelSU_SUSFS](https://github.com/zzh20188/GKI_KernelSU_SUSFS/) 本人只进行了部分修改与问题修复，请各位使用者优先考虑分叉原始仓库。

② 本仓库只提供ReSukiSU的预构建内核，对于其它KernelSU分支，请分叉本仓库或 [zzh20188/GKI_KernelSU_SUSFS](https://github.com/zzh20188/GKI_KernelSU_SUSFS/) 然后自行构建。

## 💰 特别鸣谢

[coolzyd9107](https://github.com/coolzyd9107)：仓库的创建者和所有者，但他是一个大fèiwù，很多东西都不会

[zzh20188](https://github.com/zzh20188)：他是本仓库的上游仓库作者

[zhuzhuzihan](https://github.com/zhuzhuzihan)：协助进行了大量修复和修改

[TanakaLun](https://github.com/TanakaLun)：协助进行了大量修复和修改

## 🚀 快速导航

<table>
<tr>
<td align="center" width="33%">

**📥 下载**

[Releases](https://github.com/coolzyd9107/GKI_KernelSU_SUSFS/releases)

</td>
<td align="center" width="33%">

**📋 更新日志**

[CHANGELOG](doc/CHANGELOG.md)

</td>
</tr>
</table>

---

## ⚠️ 兼容性提醒

> **注意：** 目前不支持一加 ColorOS 14、15，刷入后可能需要清除数据开机。

---

## 💡 零宽字符漏洞修复请使用 [Unicode零宽修复模块](https://t.me/real5ec1cff/268) (Xposed)

---

## 🐱 谷歌GKI发布地址：[点击跳转](https://source.android.com/docs/core/architecture/kernel/gki-release-builds?hl=zh-cn)

---

## ❗构建失败常见原因（SukiSU / SUSFS 更新不同步）

当以下两个分支的更新节奏不一致时，构建可能失败：

- SukiSU builtin 分支：<https://github.com/SukiSU-Ultra/SukiSU-Ultra/tree/builtin>
- SUSFS gki-android14-6.1 分支：<https://gitlab.com/simonpunk/susfs4ksu/-/tree/gki-android14-6.1?ref_type=heads>

例如：SUSFS 刚更新了新提交，但 SukiSU 的 `builtin` 分支还没跟进适配，这时打补丁/编译就容易失败。

如以下情况，只能等待SukiSU跟进，完成与SUSFS最新提交的适配。

<img src="assets/sukisu_eg1.png" alt="SukiSU builtin 更新记录" width="80%">
<img src="assets/susfs_eg1.png" alt="SUSFS gki-android14-6.1 更新记录" width="80%">

## 🔧 自定义提交配置
通过 [`config/config`](config/config) 文件可以指定 SUSFS 和 SukiSU 使用特定的 commit。

**什么是提交 (commit)？**

提交是一串哈希字符串，代表仓库在某个时间点的状态。例如将 sukisu 设为 `4b8644515fe6d87a109129e590ccd9d33a855dca`，即使用 1 月 30 日的 SukiSU 版本编译内核。

**为什么要指定提交？**

- 当上游仓库更新引入 bug 或兼容性问题时，可回退到稳定版本
- 当 SUSFS 与 SukiSU 版本不同步导致编译失败时，可手动指定兼容的版本

**如何获取提交哈希？**

- SUSFS: https://gitlab.com/simonpunk/susfs4ksu
- SukiSU: https://github.com/SukiSU-Ultra/SukiSU-Ultra/commits/builtin/
- 请注意：ReSukiSU请使用原版SUSFS而不是SukiSU的SUSFS分支

以 SUSFS 为例，先选择分支，再复制对应提交的哈希值：

![选择分支](assets/susfs_branch.png)
![复制提交](assets/susfs_commit.png)

```ini
# 启用自定义提交
custom=true

# SUSFS 各分支的 commit hash
gki-android12-5.10=
gki-android13-5.15=
gki-android14-6.1=
gki-android15-6.6=

# SukiSU 的 commit hash
sukisu=
```

> 留空则使用该分支的最新提交。

---

## 🛠️ 安装后推荐

### 📦 模块推荐

<table>
<tr>
<th>模块名称</th>
<th>仓库</th>
<th>频道</th>
</tr>
<tr>
<td><b>LSPosed-Irena</b></td>
<td><a href="https://github.com/re-zero001/LSPosed-Irena">GitHub</a></td>
<td><a href="https://t.me/lsposed_irena">Telegram</a></td>
</tr>
<tr>
<td><b>Zygisk Next</b></td>
<td><a href="https://github.com/Dr-TSNG/ZygiskNext">GitHub</a></td>
<td rowspan="2"><a href="https://t.me/real5ec1cff">Telegram</a></td>
</tr>
<tr>
<td><b>TrickyStore</b></td>
<td><a href="https://github.com/5ec1cff/TrickyStore">GitHub</a></td>
</tr>
</table>

### 🔧 Xposed 模块

| 模块 | 说明 |
|:---:|:---|
| **FuseFixer** | [Unicode零宽修复模块](https://t.me/real5ec1cff/268) |

---

<div align="center">

**更多内容持续更新中...**

⭐ 如果这个项目对你有帮助，请点个 Star 支持一下！

</div>
