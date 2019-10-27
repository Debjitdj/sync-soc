import React from 'react';
import './App.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import { Redirect } from 'react-router'
import Login from './Login'
import Home from './Home'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: false,
      communityName: ""
    };
  }

  setAuthenticated = (value) => {
    this.setState({authenticated: value});
  }

  setCommunityName = (name) => {
    this.setState({communityName: name});
  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            { this.state.authenticated && 
              <Route exact path="/home" component={() => <Home communityName={this.state.communityName} />} />
            }
            { this.state.authenticated && 
              <Redirect to="/home" />
            }
            <Route exact path="/login" component={() => <Login setAuthenticated={this.setAuthenticated}/>} />       

            { !this.state.authenticated &&
            <Redirect to="/login" />
            }
            </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
