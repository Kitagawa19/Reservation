# Bootstrapを入れるときの注意点
export default defineNuxtConfig({
  head: {
    script: [
      {
        src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js',
        integrity: 'sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENhcO8t22d+0pK63uXkSf',
        crossorigin: 'anonymous',
        body: true // これにより、スクリプトが<body>タグの終了直前に配置されます。
      }
    ],
  },
  css: ["bootstrap/dist/css/bootstrap.css"],
  devtools: { enabled: true }
})
を追加しないと動かなかったです
# 次の作業
自分のした予約の表示
空き日や予約されている日の一覧の表示
UIを一番意識して作ってみる