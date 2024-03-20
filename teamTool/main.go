package main

import (
	"log"
	"net/http"
	"teamTool/config"
	"teamTool/router"
	"time"
)

func main() {
	config.GetConfig()
	config.GetDB()
	route := router.NewRouter()
	s := &http.Server{
		Addr:           ":8888",
		Handler:        route,
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}
	err := s.ListenAndServe()
	if err != nil {
		log.Println("server start fail")
	} else {
		log.Println("server start success")
	}
}
