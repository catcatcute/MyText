package router

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func Cors() gin.HandlerFunc {
	return func(context *gin.Context) {
		method := context.Request.Method
		// 1. [必须]接受指定域的请求，可以使用*不加以限制，但不安全
		//context.Header("Access-Control-Allow-Origin", "*")
		context.Header("Access-Control-Allow-Origin", "http://127.0.0.1:3000")
		//fmt.Println(context.GetHeader("Origin"))
		// 2. [必须]设置服务器支持的所有跨域请求的方法
		context.Header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE, OPTIONS")
		// 3. [可选]服务器支持的所有头信息字段，不限于浏览器在"预检"中请求的字段
		context.Header("Access-Control-Allow-Headers", "Content-Type, Content-Length, Token")
		// 4. [可选]设置XMLHttpRequest的响应对象能拿到的额外字段
		context.Header("Access-Control-Expose-Headers", "Access-Control-Allow-Headers, Token")
		// 5. [可选]是否允许后续请求携带认证信息Cookir，该值只能是true，不需要则不设置
		context.Header("Access-Control-Allow-Credentials", "true")
		// 6. 放行所有OPTIONS方法
		//允许类型校验
		if method == "OPTIONS" {
			context.JSON(http.StatusOK, "ok!")
		}

		defer func() {
			if err := recover(); err != nil {

			}
		}()

		context.Next()
	}
}

// jwt
func LoginCheck() gin.HandlerFunc {
	return func(ctx *gin.Context) {

	}
}
