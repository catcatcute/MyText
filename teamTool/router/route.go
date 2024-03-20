package router

import (
	"github.com/gin-gonic/gin"
	"teamTool/api"
)

func NewRouter() *gin.Engine {
	gin.SetMode(gin.ReleaseMode)

	server := gin.Default()
	server.Use(Cors())
	server.Use(Recovery)
	// server.Use(gin.Recovery())

	//socket := RunSocekt
	user := server.Group("/user/")
	{
		user.POST("register", api.UserRegister)
		user.POST("login", api.UserLogin)
	}
	chat := server.Group("/chat/")
	{
		chat.POST("send")
	}
	return server
}

func Recovery(c *gin.Context) {
	defer func() {
		if r := recover(); r != nil {

		}
	}()
	c.Next()
}
