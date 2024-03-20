package apiStruct

type GeneralResponse struct {
	Status  bool        `json:"status"`
	ErrCode int         `json:"errCode"`
	Err     string      `json:"err"`
	Data    interface{} `json:"data"`
}

func (resp GeneralResponse) SetResponse(bool2 bool, int2 int, string2 string) {
	resp.Status = bool2
	resp.ErrCode = int2
	resp.Err = string2
}
