
import axios from "axios"
import store from '@/store/index'



// Creating an instance
const service = axios.create({
  // baseURL: 'http://raspberrypi/api/v1/',
  baseURL: 'http://127.0.0.1:5000/api/v1/',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  timeout: 10000  // 请求超时时间
})

// Add a request interceptor
service.interceptors.request.use(function (config) {
  // if(config.method === 'post') {
    if (store.state.jwt) {
      config.headers['Authorization'] = store.state.jwt
    }// POST传参序列化
    config.data = JSON.stringify(config.data)
    // console.log(config.data)
    
  // }
  return config
  }, function (error) {
    return Promise.reject(error)
    }
)

// Add a response interceptor
axios.interceptors.response.use(function (response) {
  // Do something with response data
  return response
}, function (error) {
  // Do something with response error
  // return Promise.reject(error)
  return console.log(error)
});


export default service