import React from 'react';
import { Redirect } from 'react-router'
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import './Login.css';
class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        email: "",
        password: ""
    }
  }

  handleEmailChange = (e) => {
    this.setState({email: e.target.value});
  }

  handlePasswordChange= (e) => {
    this.setState({password: e.target.value});
  }

  handleLogin = () => {
      if(this.state.email == "test" && this.state.password == "test"){
        this.props.setAuthenticated(true);
      }
      else
      alert("wrong credentials!");
  }


  render() {
    return (
      <div className="login-container">
          <div className="login-component">
            <div className="login-header">
                LOGIN
            </div>
            <div className="login-block">
                <div className="form-group">
                    <label for="exampleInputEmail1">Email address</label>
                    <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" onChange={this.handleEmailChange}/>
                    <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                </div>
                <div className="form-group">
                    <label for="exampleInputPassword1">Password</label>
                    <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" onChange={this.handlePasswordChange}/>
                </div>
                <button type="submit" className="btn btn-secondary login-button" onClick={this.handleLogin}>Login</button>
            </div>
          </div>
      </div>
    );
  }
}

export default Login;
