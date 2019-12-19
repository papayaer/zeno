import service from './request'
// import store from '@/store'


// author信息
export function author(author) {
  return service.get('users/'+author+'/')
}


// 当前author主页里的动态(包括自己的文章和自己关注人的文章,不包括收藏的文章)
export function followedPost(page, author) {
  return service.get(`users/${author}/followed/posts/?page=${page}`)
}

// 当前author主页里自己的收藏
export function favoritePost(page, author) {
  return service.get(`users/${author}/favorite/?page=${page}`)
}

// 当前author主页里只属于自己发布的文章
export function authorPost(author) {
  return service.get('users/'+author+'/posts/')
}


