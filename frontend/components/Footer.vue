<template>
  <footer class="bg-light text-center text-lg-start">
    <div class="container p-4">
      <div class="row">
        <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
          <h5 class="text-uppercase">予約サイト</h5>
          <p>
            このサイトは教室の予約を行うためのサイトです。
          </p>
        </div>
        <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
          <h5 class="text-uppercase">リンク</h5>
          <ul class="list-unstyled mb-0">
            <li>
              <NuxtLink to="/" class="text-dark">ホーム</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/" class="text-dark">会社概要</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/" class="text-dark">お問い合わせ</NuxtLink>
            </li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
          <h5 class="text-uppercase">連絡先</h5>
          <ul class="list-unstyled">
            <li>
              <a href="#!" class="text-dark">メール: info@example.com</a>
            </li>
            <li>
              <a href="#!" class="text-dark">電話: 123-456-7890</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent',
}
</script>
