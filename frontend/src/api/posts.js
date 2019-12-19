import service from './request'

// 全部post并分页
export function article(page) {
  return service.get(`posts/?page=${page}`)
}

// post单页
export function details(postId) {
  return service.get('posts/'+ postId)
}

// 写post
export function writePost(postBody) {
  return service.post('posts/', postBody)
}

// 当前post的评论
export function get_post_comments(postId) {
  return service.get(`posts/${postId}/comments/`)
}