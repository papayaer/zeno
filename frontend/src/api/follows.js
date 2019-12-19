import service from './request'
// import store from '@/store'


// 当前author的粉丝
export function follower(page, author) {
  return service.get(`users/${author}/followers/?page=${page}`)
}

// 当前author的关注者
export function followed(page, author) {
  return service.get(`users/${author}/followed/?page=${page}`)
}

// 是否已关注
export function hasFollow(author) {
  return service.get('users/'+author+'/following/')
}

// 加关注
export function doFollow(author) {
  return service.post('users/'+author+'/follow/')
}

// 取消关注
export function doUnFollow(author) {
  return service.post('users/'+author+'/unfollow/')
}
