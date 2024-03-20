package config

import (
	"encoding/json"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"io"
	"log"
	"os"
)

type AllConfig struct {
	MysqlAddr string
}

var ConfigData *AllConfig

var MysqlDB *gorm.DB

func GetConfig() {
	file, err := os.Open("../config.json")
	if err != nil {
		log.Println("read config fail")
		return
	}
	bytes, _ := io.ReadAll(file)
	err = json.Unmarshal(bytes, ConfigData)
	if err != nil {
		log.Println("unmarshal config fail")
		return
	}
	defer func() {
		if err != nil {
			panic(err)
		}
	}()
}

func GetDB() {
	var err error
	MysqlDB, err = gorm.Open(mysql.Open(ConfigData.MysqlAddr), &gorm.Config{})
	if err != nil {
		log.Println("connect db fail")
		panic(err)
	}
}
