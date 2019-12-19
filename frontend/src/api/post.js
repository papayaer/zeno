var now = new Date();
var nowY = now.getFullYear();
var nowM = now.getMonth();
var nowD = now.getDay();
var nowStr = nowY+'年'+nowM+'月'+nowD+'日';
const posts = {
  '1': {
    id: 1,
    author: 'consectetur adipisicing',
    data: nowStr,
    img: '/assets/img/1-900x325.jpg',
    title: 'Nesciunt aspernatur eaque similique laudantium a',
    body: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda modi inventore, totam vero consequuntur, aut animi veritatis tempora nulla facere placeat velit illum explicabo dicta enim ipsum. Vitae ducimus, ratione.'
  },
  '2': {
    id: 2,
    author: 'Sit enim ipsam mollitia',
    data: nowStr,
    img: '/assets/img/2-900x325.jpg',
    title: 'Consequatur adipisci neque possimus quod ut quidem omnis numquam dolorum',
    body: 'Consectetur adipisicing elit. Sit enim ipsam mollitia repellat nemo, accusantium? Fugit id ipsam libero vitae quas perferendis, delectus a amet perspiciatis iusto. Quia, quam, culpa.'
  },
  '3': {
    id: 3,
    author: 'ratione laudantium',
    data: nowStr,
    img: '/assets/img/3-900x325.jpg',
    title: 'Adipisci alias ullam est accusamus',
    body: 'Adipisci repellendus ratione laudantium nisi eaque voluptatem fuga quod hic, explicabo amet at laborum maiores ducimus et a vel quidem dolorem modi.'
  },
  '4': {
    id: 4,
    author: 'tempora molestiae',
    data: nowStr,
    img: '/assets/img/4-900x325.jpg',
    title: 'Dolor sit amet, consectetur adipisicing elit',
    body: 'Vitae est numquam, dolore, ipsum tempora molestiae. Ut optio natus velit eaque tempora commodi dolor doloremque error quidem labore, incidunt odit est nobis numquam. Ullam quas minima, neque modi reiciendis consequuntur inventore!'
  },
  '5': {
    id: 5,
    author: 'harum dolorem nam',
    data: nowStr,
    img: '/assets/img/5-900x325.jpg',
    title: 'Veritatis aut repellendus, quidem nesciunt consequatur nulla sed itaque',
    body: 'Expedita voluptate similique ad harum dolorem nam ipsa repellat quos, autem eius magni minima, asperiores nobis repudiandae ut quibusdam atque! Delectus atque veniam labore suscipit ullam, consequuntur dicta, tenetur est nulla, quod obcaecati similique?'
  },
  '6': {
    id: 6,
    author: 'ipsum asperiores',
    data: nowStr,
    img: '/assets/img/6-900x325.jpg',
    title: 'Culpa quo animi ut temporibus, et distinctio facere perspiciatis saepe sunt unde',
    body: 'Iusto magni quasi recusandae autem ipsum asperiores consequatur explicabo, vero nam iste quas sequi reiciendis quod, quos!'
  },
  '7': {
    id: 7,
    author: 'maxime omnis',
    data: nowStr,
    img: '/assets/img/7-900x325.jpg',
    title: 'Molestiae quod consectetur enim modi unde expedita dicta placeat?',
    body: 'Aliquam laudantium mollitia quo sint maxime omnis repellendus beatae. Consequuntur molestias odio sapiente. Officia minima, nisi! Tempora vero, architecto ducimus animi nostrum nobis aliquid eligendi illo, facilis temporibus.'
  },
  '8': {
    id: 8,
    author: 'Sit amet',
    data: nowStr,
    img: '/assets/img/8-900x325.jpg',
    title: 'Sit amet, consectetur adipisicing elit. Incidunt, commodi!',
    body: 'Accusamus culpa maxime harum minus ipsa ea qui, blanditiis sequi debitis. Temporibus quisquam consequatur dolor, aliquid odio nulla dolorum animi quasi et! Reiciendis ipsum repellendus quaerat explicabo, laboriosam amet, temporibus at sed voluptatibus, minima quia.'
  },
  '9': {
    id: 9,
    author: 'voluptate a nostrum',
    data: nowStr,
    img: '/assets/img/9-900x325.jpg',
    title: 'Inventore ducimus, voluptate a nostrum molestiae non',
    body: 'Similique officia recusandae, at labore quae, minus aspernatur cupiditate repellendus optio nesciunt iure aliquid praesentium, omnis, quas est natus temporibus aliquam vero.'
  },
  '10': {
    id: 10,
    author: 'consequatur',
    data: nowStr,
    img: '/assets/img/10-900x325.jpg',
    title: 'Voluptatum nisi, nostrum eaque consequatur officiis similique!',
    body: 'Soluta eius itaque, molestiae laborum! Facere velit reiciendis quis architecto vel minima consequuntur voluptates temporibus consequatur, aperiam maiores! Perferendis quos architecto quaerat, aliquid earum culpa labore.'
  },
  '11': {
    id: 11,
    author: 'doloremque',
    data: nowStr,
    img: '/assets/img/11-900x325.jpg',
    title: 'Perspiciatis non voluptatibus quo ab doloremque accusantium',
    body: 'Eligendi similique excepturi cumque nemo modi voluptates mollitia atque doloribus, laborum magnam itaque a! Dignissimos expedita vel minus impedit laudantium.'
  },
  '12': {
    id: 12,
    author: 'obcaecati',
    data: nowStr,
    img: '/assets/img/12-900x325.jpg',
    title: 'Quam id laudantium debitis perferendis neque perspiciatis!',
    body: 'Deleniti blanditiis iste cupiditate ea obcaecati corporis, quas nobis possimus molestiae. Sed, minima.'
  },
  '13': {
    id: 13,
    author: 'adipisicing',
    data: nowStr,
    img: '/assets/img/13-900x325.jpg',
    title: 'Nesciunt aspernatur eaque similique laudantium a',
    body: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda modi inventore, totam vero consequuntur, aut animi veritatis tempora nulla facere placeat velit illum explicabo dicta enim ipsum. Vitae ducimus, ratione.'
  },
  '14': {
    id: 14,
    author: 'adipisicing',
    data: nowStr,
    img: '/assets/img/14-900x325.jpg',
    title: 'Consequatur adipisci neque possimus quod ut quidem omnis numquam dolorum',
    body: 'Consectetur adipisicing elit. Sit enim ipsam mollitia repellat nemo, accusantium? Fugit id ipsam libero vitae quas perferendis, delectus a amet perspiciatis iusto. Quia, quam, culpa.'
  },
  '15': {
    id: 15,
    author: 'repellendus',
    data: nowStr,
    img: '/assets/img/15-900x325.jpg',
    title: 'Adipisci alias ullam est accusamus',
    body: 'Adipisci repellendus ratione laudantium nisi eaque voluptatem fuga quod hic, explicabo amet at laborum maiores ducimus et a vel quidem dolorem modi.'
  },
  '16': {
    id: 16,
    author: 'tempora',
    data: nowStr,
    img: '/assets/img/16-900x325.jpg',
    title: 'Dolor sit amet, consectetur adipisicing elit',
    body: 'Vitae est numquam, dolore, ipsum tempora molestiae. Ut optio natus velit eaque tempora commodi dolor doloremque error quidem labore, incidunt odit est nobis numquam. Ullam quas minima, neque modi reiciendis consequuntur inventore!'
  },
  '17': {
    id: 17,
    author: 'consequatur',
    data: nowStr,
    img: '/assets/img/17-900x325.jpg',
    title: 'Veritatis aut repellendus, quidem nesciunt consequatur nulla sed itaque',
    body: 'Expedita voluptate similique ad harum dolorem nam ipsa repellat quos, autem eius magni minima, asperiores nobis repudiandae ut quibusdam atque! Delectus atque veniam labore suscipit ullam, consequuntur dicta, tenetur est nulla, quod obcaecati similique?'
  },
  '18': {
    id: 18,
    author: 'recusandae autem',
    data: nowStr,
    img: '/assets/img/18-900x325.jpg',
    title: 'Culpa quo animi ut temporibus, et distinctio facere perspiciatis saepe sunt unde',
    body: 'Iusto magni quasi recusandae autem ipsum asperiores consequatur explicabo, vero nam iste quas sequi reiciendis quod, quos!'
  },
  '19': {
    id: 19,
    author: 'laudantium',
    data: nowStr,
    img: '/assets/img/19-900x325.jpg',
    title: 'Molestiae quod consectetur enim modi unde expedita dicta placeat?',
    body: 'Aliquam laudantium mollitia quo sint maxime omnis repellendus beatae. Consequuntur molestias odio sapiente. Officia minima, nisi! Tempora vero, architecto ducimus animi nostrum nobis aliquid eligendi illo, facilis temporibus.'
  },
  '20': {
    id: 20,
    author: 'Accusamus',
    data: nowStr,
    img: '/assets/img/20-900x325.jpg',
    title: 'Sit amet, consectetur adipisicing elit. Incidunt, commodi!',
    body: 'Accusamus culpa maxime harum minus ipsa ea qui, blanditiis sequi debitis. Temporibus quisquam consequatur dolor, aliquid odio nulla dolorum animi quasi et! Reiciendis ipsum repellendus quaerat explicabo, laboriosam amet, temporibus at sed voluptatibus, minima quia.'
  },
  '21': {
    id: 21,
    author: 'at labore quae',
    data: nowStr,
    img: '/assets/img/21-900x325.jpg',
    title: 'Inventore ducimus, voluptate a nostrum molestiae non',
    body: 'Similique officia recusandae, at labore quae, minus aspernatur cupiditate repellendus optio nesciunt iure aliquid praesentium, omnis, quas est natus temporibus aliquam vero.'
  },
  '22': {
    id: 22,
    author: 'molestiae laborum',
    data: nowStr,
    img: '/assets/img/22-900x325.jpg',
    title: 'Voluptatum nisi, nostrum eaque consequatur officiis similique!',
    body: 'Soluta eius itaque, molestiae laborum! Facere velit reiciendis quis architecto vel minima consequuntur voluptates temporibus consequatur, aperiam maiores! Perferendis quos architecto quaerat, aliquid earum culpa labore.'
  },
  '23': {
    id: 23,
    author: 'similique excepturi',
    data: nowStr,
    img: '/assets/img/23-900x325.jpg',
    title: 'Perspiciatis non voluptatibus quo ab doloremque accusantium',
    body: 'Eligendi similique excepturi cumque nemo modi voluptates mollitia atque doloribus, laborum magnam itaque a! Dignissimos expedita vel minus impedit laudantium.'
  },
  '24': {
    id: 24,
    author: 'Deleniti blanditiis',
    data: nowStr,
    img: '/assets/img/14-900x325.jpg',
    title: 'Quam id laudantium debitis perferendis neque perspiciatis!',
    body: 'Deleniti blanditiis iste cupiditate ea obcaecati corporis, quas nobis possimus molestiae. Sed, minima.'
  },
  '25': {
    id: 25,
    author: 'consectetur',
    data: nowStr,
    img: '/assets/img/25-900x325.jpg',
    title: 'Nesciunt aspernatur eaque similique laudantium a',
    body: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda modi inventore, totam vero consequuntur, aut animi veritatis tempora nulla facere placeat velit illum explicabo dicta enim ipsum. Vitae ducimus, ratione.'
  },
  '26': {
    id: 26,
    author: 'Consectetur adipisicing elit',
    data: nowStr,
    img: '/assets/img/26-900x325.jpg',
    title: 'Consequatur adipisci neque possimus quod ut quidem omnis numquam dolorum',
    body: 'Consectetur adipisicing elit. Sit enim ipsam mollitia repellat nemo, accusantium? Fugit id ipsam libero vitae quas perferendis, delectus a amet perspiciatis iusto. Quia, quam, culpa.'
  },
  '27': {
    id: 27,
    author: 'Adipisci repellendus',
    data: nowStr,
    img: '/assets/img/27-900x325.jpg',
    title: 'Adipisci alias ullam est accusamus',
    body: 'Adipisci repellendus ratione laudantium nisi eaque voluptatem fuga quod hic, explicabo amet at laborum maiores ducimus et a vel quidem dolorem modi.'
  },
  '28': {
    id: 28,
    author: 'ipsum tempora molestiae',
    data: nowStr,
    img: '/assets/img/21-900x325.jpg',
    title: 'Dolor sit amet, consectetur adipisicing elit',
    body: 'Vitae est numquam, dolore, ipsum tempora molestiae. Ut optio natus velit eaque tempora commodi dolor doloremque error quidem labore, incidunt odit est nobis numquam. Ullam quas minima, neque modi reiciendis consequuntur inventore!'
  },
  '29': {
    id: 29,
    author: 'voluptate',
    data: nowStr,
    img: '/assets/img/24-900x325.jpg',
    title: 'Veritatis aut repellendus, quidem nesciunt consequatur nulla sed itaque',
    body: 'Expedita voluptate similique ad harum dolorem nam ipsa repellat quos, autem eius magni minima, asperiores nobis repudiandae ut quibusdam atque! Delectus atque veniam labore suscipit ullam, consequuntur dicta, tenetur est nulla, quod obcaecati similique?'
  },
  '30': {
    id: 30,
    author: 'Iusto magni quasi',
    data: nowStr,
    img: '/assets/img/27-900x325.jpg',
    title: 'Culpa quo animi ut temporibus, et distinctio facere perspiciatis saepe sunt unde',
    body: 'Iusto magni quasi recusandae autem ipsum asperiores consequatur explicabo, vero nam iste quas sequi reiciendis quod, quos!'
  }
}

export function fetchData() {
  // fake an api request
  return posts
}

export function getPost(id, cb) {
  // fake an api request
  setTimeout(() => {
    if (posts[id]) {
      cb(null, posts[id])
    } else {
        cb(new Error('Post not found.'))
      } 
  }, 100);
  
}