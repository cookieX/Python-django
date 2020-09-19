# RET-Zurichteam API

## Backend API Link. https://hackzurich2020.herokuapp.com/ or /admin/

### Small documents about API description.

- Login API : https://hackzurich2020.herokuapp.com/api/1/oauth/token/ **Need to provide data for most method like data: `grant_type=password&username=${this.state.username}&password=${this.state.password}&client_id=${CLIENT_ID}`**

- Registration API: https://hackzurich2020.herokuapp.com/api/1/user/register/ **Once User will register they will get an confirmation email on register email id .**

- Edit User API: https://hackzurich2020.herokuapp.com/api/1/user/edit/me/ Its authenticated so only loggineduser can edit his own profile

- Change password : https://hackzurich2020.herokuapp.com/api/1/user/change/password/

- User Profile View : https://hackzurich2020.herokuapp.com/api/1/user/{usernameofuser}/

- Forget password : https://hackzurich2020.herokuapp.com/users/password-reset/ **Once user will use their email id for forget password they will receive link to forget password on his/her email .**
