package api

import (
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
	"log"
	"net/http"
	"teamTool/apiStruct"
	"teamTool/config"
	"teamTool/model"
	"time"
)

func UserRegister(c *gin.Context) {
	req := &model.User{}
	resp := apiStruct.GeneralResponse{}
	defer func() {
		c.JSON(http.StatusOK, resp)
	}()
	err := c.ShouldBind(req)
	if err != nil {
		log.Println("bind err")
		return
	}
	req.CreateAt = time.Now()
	err = config.MysqlDB.Transaction(func(tx *gorm.DB) error {
		if err := tx.Create(req).Error; err != nil {
			return err
		}
		return nil
	})
	if err != nil {
		log.Println("create fail,add data fail")
		resp.SetResponse(true, 1, err.Error())
		return
	}
}

func UserLogin(c *gin.Context) {
	resp := apiStruct.GeneralResponse{}
	defer func() {
		c.JSON(http.StatusOK, resp)
	}()
}
