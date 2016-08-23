package main

import (
    "fmt"
    "github.com/axgle/mahonia"
    "io/ioutil"
    "net/http"
    "regexp"
    "strings"
)

func main() {
    // 用户 Cookie
    var cookie string = "oMVX_2132_saltkey=BQ1dWrGn;oMVX_2132_auth=95f6c%2BOg2r7RFCtaANsi%2FDKG8KHdIZeQ1PEfL79b8NVnVBZiyo%2F8RaRFCDqvO8qC2o34ND%2FpV1gDVYiNNOujs%2FZy048;"
    // regexp.MustCompile 返回一个值, 可用于常量定义
    // regexp.Compile 返回两个值, 第二个值表示错误
    hash_pattern := regexp.MustCompile(`formhash=(.+)">.+?</a>`)
    resp_pattern := regexp.MustCompile(`<div class="c">\s*?(.+?)<a href="`)

    client := &http.Client{}

    request, _ := http.NewRequest("GET", "http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign", nil)

    request.Header.Set(
        "Cookie",
        cookie)

    res, _ := client.Do(request)

    body_, _ := ioutil.ReadAll(res.Body)
    // fmt.Println(string(body_))

    defer res.Body.Close()

    formhash := hash_pattern.FindStringSubmatch(string(body_))[1]
    // fmt.Println(formhash)

    req, _ := http.NewRequest(
        "POST",
        "http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&inajax=1",
        strings.NewReader("qdxq=kx&qdmode=2&todaysay=&fastreply=1&formhash=" + formhash))

    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
    req.Header.Set("Cookie", cookie)

    response, _ := client.Do(req)

    body, _ := ioutil.ReadAll(response.Body)

    defer response.Body.Close()

    output := mahonia.NewDecoder("GBK").ConvertString(string(body))

    result := resp_pattern.FindStringSubmatch(output)[1]

    fmt.Println(result)
}
