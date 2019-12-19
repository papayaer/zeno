import service from './request'


// 当前author的讨论
export function comment(page, author) {
  return service.get(`users/${author}/comments/?page=${page}`)
}

// 写评论
export function writeComment(postId, Body) {
  return service.post(`posts/${postId}/comments/`, Body)
}