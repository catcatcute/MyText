

## 网络

从输入网址，到页面显示，那些过程

### tcp连接

#### 三次握手

客户端-服务器-客户端

1. 建立连接：客户端发送一个连接请求报文段（SYN）到服务器。服务器收到请求后，发送一个确认报文段（SYN-ACK）给客户端。客户端再发送一个确认报文段（ACK）给服务器，建立连接。
2. 数据传输：建立连接后，客户端和服务器可以通过TCP连接进行数据的传输。数据被划分成小的数据块（数据段），每个数据段带有序号。发送方将数据段发送给接收方，并等待接收方发送确认信息，表示已成功接收。
3. 断开连接：当数据传输完毕或者一方需要断开连接时，会发送一个断开连接请求报文段（FIN）给对方。对方收到请求后，会发送一个确认报文段（ACK）作为确认。然后对方也发送一个断开连接请求报文段（FIN）给发起断开的一方，发起断开的一方发送一个确认报文段（ACK）作为确认。这样，两端都确认断开连接，完成断开连接的过程。
   
#### 四次挥手

双向连接都要断开，客户端-服务端-服务端-客户端

### 杂

tcp一个包的大小由MTU（最大传输单元）决定，一般为1500字节，由于ip和tcp的头部的开销，有效数据为1460字节，如果一次性发送的数据超过了这个分为，那就会分段，多个数据包发送，在接受的时候重组

对于int64和string的数据，采用转换二进制的方式传输 

int64转为8字节的二进制数据，按照网络字节序（大段字节序）发送

string一般会选择一种编码方式（utf-8等），在接受的时候也要用相同的方式解码

### http连接（go实现）

http请求，接收方定义结构体之后，双方使用json加密，接收方需要使用类型断言解析为结构体内容  找方法一键解析？



#### get

```go
url := "http://api" 
request, err := http.NewRequest(http.MethodGet, url, bytes.NewReader([]byte{}))
client := http.Client{Timeout: 2 * time.Minute}
resp1, err := client.Do(request)
respMain, err := ioutil.ReadAll(resp1.Body)
if err != nil {
    log.Println(err.Error())
    resp.SetGeneral(true, 3, err.Error())
    return
}
```



#### post

```go

lossdataReq := &puppy_protocol.ReqCheckLoss{Time: timeRange, Servers: server, Channels: channel}
lossdataContent, err := json.Marshal(lossdataReq)
if err != nil {
 fmt.Println(err)
}
reader = bytes.NewReader(lossdataContent)
req, err := http.NewRequest("POST", url+"/api/analysis/lvlost", reader)
if err != nil {
 fmt.Println(err)
 return
}
req.Header.Set("Authorization", token)
resp, err = client.Do(req)
if err != nil {
 fmt.Println(err.Error())
}
body, err = ioutil.ReadAll(resp.Body)
if err != nil {
 fmt.Println("读取响应失败：", err)
 return
}
// 打印响应内容
fmt.Println(string(body))
reader1 = bytes.NewReader(body)
//// 使用 reader 进行后续操作
//// 例如：解析为结构体
var lossdataResp puppy_protocol.RespGeneral
err = json.NewDecoder(reader1).Decode(&lossdataResp)
if err != nil {
 fmt.Println(err.Error())
 return
}
```

#### session

超时协议进行功能分割，加状态锁（全局变量） 待定

项目开发，网关，外网访问

### RPC(远程过程调用)



### 序列化和反序列化

#### idl

##### json

##### protobuf

## linux

### 文件权限

rwxrwxrwx 9位

r 读取权限  w写入权限  x执行权限

前三位，文件所有者owner，创建文件的用户

中间三位，所属组

后三位，其他人



```
grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' /var/log/apache/access.log | sort | uniq -c | sort -nr
```

## 正则

常用正则





### 指令

## 设计模式

### 单例

#### 饿汉

静态变量，声明时创建，直接new出来，或者在init里面初始化，在程序运行期间永久存在，当对象过大时会有内存浪费

#### 懒汉

在获取这个对应的对象的时候才会被创建，且只会创建一次

考虑线程安全

多线程的情况下，每个线程抢占同一个资源，可能会造成同一个对象被多次创建的情况，破坏单例模式

加锁

在初始化之前上锁，保证每次只有一下线程操作对象，解决并发问题，但是效率较低

优化

双重检查锁，只有在对象没有被初始化的时候，才需要进行上锁和解锁

```go
type singleton struct {
 
}

var instance *singleton
var lock sync.Mutex

func GetInstance() *singleton {
 if instance == nil{
  lock.Lock()
  if instance == nil{
   instance = new(singleton)
  }
  lock.Unlock()
 }
 return instance
}
```

原子操作

sync.once  在程序运行的过程中，只运行一次回调函数

```go
type singleton struct {
 
}

var instance *singleton
var once sync.Once
func GetInstance() *singleton {
 once.Do(func() {
  instance = new(singleton)
 })
 return instance
}
```

## DB

### 索引

inno索引结构    B+树

### sql

mysql -u name -p 连接

select * from

update from where set

delete from where



一般单条sql能查询的最多数据为2的20次方，1048576行

where本质是过滤

having 可以使用聚合函数作为筛选条件

外连接，内连接

外连接保留原来的数据，左外连接保留左侧，右外保留右侧

内连接取两表公共数据

limit对group无效？

第n高，窗口函数

like  %test%

.sql.gz

1. 打开终端窗口，并定位到要保存文件的目录。

2. 使用wget命令下载.sql.gz文件，例如：

   ```
   Copy Codewget http://example.com/file.sql.gz
   ```

   将URL替换为实际的文件URL。

3. 使用gunzip命令对文件进行解压缩，例如：

   ```
   Copy Codegunzip file.sql.gz
   ```

   将"file.sql.gz"替换为你下载的实际文件名。


4. 解压缩后会得到一个.sql文件，使用适当的工具（如MySQL命令行工具或其他数据库管理工具）来读取和获取数据。例如，如果你使用MySQL：

   ```
   Copy Codemysql -u <用户名> -p <数据库名> < file.sql
   ```

   将"<用户名>"替换为你的MySQL用户名，"<数据库名>"替换为要导入数据的目标数据库名。

   这将执行.sql文件中的SQL语句，并将数据导入到指定的数据库中。

解压缩之后导入mysql，建立连接，访问数据

### 单表查询

单表查询优化有以下几个方面可以考虑：

1. 添加索引：通过给查询字段添加索引，可以加快查询速度。一般情况下，可以考虑给经常用于查询条件和排序的字段添加索引。
2. 优化查询条件：尽量使用WHERE子句来限定查询的范围，避免全表扫描。可以使用AND和OR来组合多个条件，充分利用索引。
3. 避免使用SELECT *：尽量指定需要查询的字段，避免查询不需要的字段，减少数据传输和内存消耗。
4. 使用合适的数据类型：根据字段的特性和数据范围，选择合适的数据类型来存储数据，减少存储和查询的开销。
5. 使用JOIN替代子查询：有时候可以使用JOIN语句来替代子查询，提高查询效率。
6. 使用LIMIT来限制结果集：如果查询只需要一部分结果，可以使用LIMIT来限制结果集的大小，减少数据传输和内存消耗。
7. 避免重复查询：在查询结果中可能存在重复的数据，可以使用DISTINCT来去除重复。
8. 定期进行表维护：定期进行表的维护，包括优化表结构、重建索引、更新统计信息等，以保证查询的性能。

#### 窗口函数

用于重复执行某一段sql

order by 列名，排序，默认升序，desc降序

limit x,y限制从x+1开始查询（忽略x条记录），查询y条记录

offset忽略

limit中的offset过大导致的性能问题

in 某一列

### xorm

get单条数据

【】*struct

find(&struct)多条数据

## nginx

```
nginx -t -c /path/to/nginx.conf
```

查看nginx的位置

nginx -v 版本

运行nginx，master主进程，读取并检验配置文件，worker子进程来接受响应

多进程启动

修改配置文件之后进行reload，子进程关闭外部访问，余留一段时间处理当前的请求，处理完毕之后杀死进程

### conf 配置文件

#### worker_processes   子进程数目 

#### worker_conneticon 

一个进程可以创造多少个连接，默认1024

#### http

include 引用配置文件

#### mime.types 

类型，在协议头中告诉客户端，返回的文件是什么类型的

某文件需要用某种类型返回，在mime.types里面添加

default_type ￥

默认类型

#### sendfile 

0拷贝，响应过程 

关闭sendfile,nginx向内存当中读取目标文件，再发送给网络接口缓存，网络接口缓存返回响应

开启，nginx发送sendfile信号给网络接口，网络接口去内存当中读取文件，减少了文件的拷贝次数

#### keepalive_timeout 

超时，tcp长连接，代理websocket

#### upstream

#### server 一个虚拟主机 vhost

listen 一个主机监听的端口号

server_name localhost 域名、主机名（必须可以被解析）

##### location 

url查到。 域名之后跟的子目录

## docker

环境镜像

docker

容器，将运行环境和项目，创建一个镜像运行在后台当中

和本地完全相同的环境，

### dockerfile



## k8s

## 算法

### dfs

前序 中左右

中序 左中右

### 二叉搜索树

根节点的值大于左子树所有节点的值，小于右子树所有节点的值，左子树和右子树同样遵循规则

平衡二叉树



### 回溯

记录当前位置，找到回溯的临界判断条件，提前剪枝

```
dfs(当前条件，目标条件){
//临界判断，一般判断边界情况
//判断此情况是否满足条件，满足当前的部分情况，继续dfs，已经不满足，提前结束检索，剪枝
}
```

### 排序

#### 冒泡

两两关键字，交换，知道没有反序的记录为止

优化：上一轮没有产生交换，跳过当前轮

#### 插入排序

直接插入

#### 希尔排序

先分组，再进行插入排序

#### 堆排序

没有要求左右孩子节点的值的大小关系

升序 大顶堆：每一个节点的值，都大于等于他的左右子节点的值

降序 小顶堆：

#### 快速排序

左右游标，交换，左右分割，再次重复，直到元素为1

### 搜索

二分    必须是有序的队列

mid left/2+right/2

重复出现，考虑=的情况

找插入位置，前一个小，当前位置大

先增后减  找最大

先减后增  找最小

### 贪心

### dp

## go模块

位运算符

|   运算符 或 

进制转换

defer 的执行顺序是后进先出

短变量只能在函数内部使用

### 数据结构

#### 数组


数组是值类型，想要改变数组的值，要传指针

长度是类型的组成部分

#### 切片slice

切片在make出来的时候会有底层数组，创建切片的时候会动态分配底层数组的长度，对切片进行追加的时候，超过的切片的容量cap，也会进行底层数组重新分配，策略一般为翻倍

#### map

总结来说，Go语言中map的底层逻辑实现是基于哈希表，使用哈希函数将键值对映射到对应的存储桶中，并通过链表处理哈希冲突。在插入和查找操作时，根据哈希值找到存储桶，并在链表中执行相应的操作。当负载因子超过阈值时，会触发扩容操作。这样，map在平均情况下具有O(1)的插入、查找和删除操作的时间复杂度。

##### make和new

new(T) 会为 T 类型的新值分配已置零的内存空间，并返回地址（指针），即类型为 `*T`的值。换句话说就是，返回一个指针，该指针指向新分配的、类型为 T 的零值。适用于值类型，如数组、结构体等。

make(T,args) 返回初始化之后的 T 类型的值，这个值并不是 T 类型的零值，也不是指针 `*T`，是经过初始化之后的 T 的引用。make() 只适用于 slice、map 和 channel.

#### rwmap

一个map结构，一个rwmutex锁，读写锁，读不受限制，在写入的时候，必须等所有的锁释放

#### syncmap

开箱即用的带锁的map，互斥锁

### 文件

```go
写入，忽略特殊字符
var data []byte
buf := bytes.NewBuffer(data)
encoder := json.NewEncoder(buf)
encoder.SetEscapeHTML(false)	encoder.SetIndent("", "  ")
err = encoder.Encode(workdata)
fmt.Println(buf.String())
File, err := os.OpenFile(fileName, os.O_CREATE|os.O_TRUNC|os.O_WRONLY, 0777)
File.WriteString(buf.String())
File.Close()
```

### 并发

#### channel

无缓冲通道

发送时，必须有人接受才能成功，没有接受，会阻塞形成死锁

有缓冲通道

#### gmp

单进程时代，都是串行运行

多进程/多线程，大部分时间用在调度，分配资源太多，创建、切换、销毁进程

原线程为内核级线程

协程引进，用户级线程

线程缺点：高内存占用、高消耗cpu资源

协程有点：占用内存更小（几 kb），调度更灵活 (runtime 调度)



协程是主动让出，线程抢占

n：1

某个程序用不了硬件的多核加速能力

一旦某协程阻塞，造成线程阻塞，本进程的其他协程都无法执行了，根本就没有并发的能力

1：1

协程的创建、删除和切换的代价都由 CPU 完成，有点略显昂贵了

m：n

m协程对n线程

g协程，m线程，p处理器

Processor，它包含了运行 goroutine 的资源，如果线程想运行 goroutine，必须先获取 P，P 中还包含了可运行的 G 队列

全局队列

p的本地队列

m所持有的p，从p中获取g，如果p中的g为空，则尝试从全局队列中拿一批g，或尝试从其他队列偷一批g放进本线程持有的p





### 函数上锁

```go
var mutex int32
if !atomic.CompareAndSwapInt32(&ResetMutex, 0, 1) {
	log.Println("ResetServerOpenTime reset fail")
	resp.SetGeneral(false, 1, "busy")
	return
}
defer func(){
    atomic.StoreInt32(&ResetMutex, 0)
}
```



### 垃圾回收

c，c++手动

python，java，go自动

垃圾回收主要针对堆上的内存

堆内存是程序共享的内存，需要通过gc回收

栈是线程的专用内存，存放函数中的局部变量及调用栈，执行完之后编译器可以直接释放

内存管理组件，分为赋值器Mutator和回收器Collector

赋值器本质上是指用户态的代码，为对象在堆上申请内存

垃圾回收器负责回收堆上的内存空间

### csv

文件读取

```go
//数据写入到csv文件
t1 := time.Now().UnixNano()
//首行
var titles string
titles = "dsadada\n"

var stringBuilder strings.Builder
stringBuilder.WriteString(titles)

var i int
for i = 0; i < len(datalist); i++ {
   dataString := fmt.Sprintf("%d,%d,%d,%s\n", datalist[i].Lv, datalist[i].num1, datalist[i].num2, datalist[i].percent)
   stringBuilder.WriteString(dataString)
}
filename := "./test.csv"
file, _ := os.OpenFile(filename, os.O_RDWR|os.O_CREATE, os.ModeAppend|os.ModePerm)
dataString := stringBuilder.String()
file.WriteString(dataString)
file.Close()

t2 := time.Now().UnixNano()
t := t2 - t1
fmt.Printf("writeToCsv总共%d条数据，总耗时%d毫秒\n", i, t/1000000)
```

前端返回

```go
buf := &bytes.Buffer{}

writer := csv.NewWriter(buf)
writer.Write([]string{
   "玩家Id", "账号", "昵称", "区服", "等级", "战力", "是否在线", "封号状态", "总充值", "光元", "曾用名", "注册区服", "注册时间", "最后登录时间", "最后登出时间",
})
for _, row := range dataList {
   writer.Write([]string{
      fmt.Sprintf("%d", row.Uid),
      row.Account,
      row.NickName,
      fmt.Sprintf("%d", row.ServerId),
      row.ServerName,
      fmt.Sprintf("%d", row.Lv),
      fmt.Sprintf("%d", row.Power),
      fmt.Sprintf("%d", row.State),
      fmt.Sprintf("%d", row.Banned),
      fmt.Sprintf("%d", row.AllRecharge),
      fmt.Sprintf("%d", row.Token),
      row.OldNick,
      time.Unix(row.RegisterTime, 0).String(),
      time.Unix(row.LastLogin, 0).String(),
      time.Unix(row.LastLogout, 0).String(),
   })
}

// 3. 刷新Writer对象，将缓冲区中的数据写入到输出流中
writer.Flush()

// 4. 设置响应头部信息，指定返回的内容类型为CSV文件
c.Header("Content-Description", "File Transfer")
c.Header("Content-Disposition", "attachment; filename=playerInfo.csv")
c.Data(http.StatusOK, "text/csv", buf.Bytes())
```

### 排序

```go
func lessFn(objs []*testdata, i, j int) bool {
	return objs[i].Lv < objs[j].Lv
}
sort.Slice(datalist, func(i, j int) bool {
   return lessFn(datalist, i, j)
})
```

### 百分比

```go
func DimalToPercentage(decimal float64) (string, error) {
   percentage := decimal * 100
   percentageStr := strconv.FormatFloat(percentage, 'f', 2, 64) + "%"
   return percentageStr, nil
}
```

### 定时任务

corn时间轮

正式实现，每个定时任务单独开协程，设置定时器

time.newticker  设置定时