import service from './request'

export function authentication(userData) {
  return service.post('login/', userData)
}

export function register(userData) {
  return service.post('register/', userData)
}

export function up_user(author,userData) {
  return service.put('users/'+author+'/', userData)
}

export function ref_user_info(author) {
  return service.get('users/'+author+'/ref/')
}