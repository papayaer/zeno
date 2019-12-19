import service from './request'
// import store from '@/store'


// 收藏了吗?
export function hasFavorite(postid) {
  return service.get('posts/'+postid+'/favoriting/')
}

// 加收藏
export function doFavorite(postid) {
  return service.post('posts/'+postid+'/favorite/')
}

// 取消收藏
export function doUnFavorite(postid) {
  return service.post('posts/'+postid+'/unfavorite/')
}