import React from 'react';
import './Home.css';
import Header from './Header'
import Calender from './Calender'
class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      today: new Date()
    }
  }

  // setMunday = (d) => {
  //   this.setState({monday: d});
  // }

  // setSunday = (d) => {
  //   this.setState({sunday: d});
  // }

  changeweek = (value) => {
    var d = this.state.today;
    var day = d.getDay();
    var diff = d.getDate() - day + value;
    this.setState({today: new Date(d.setDate(diff))})
  }

  render() {
    
    return (
      <div className="home-container">
          <Header
            today={this.state.today}
            // monday={this.state.monday}
            // sunday={this.state.sunday}
            // setMunday={this.setMunday}
            // setSunday={this.setSunday}
            changeweek={this.changeweek}
          />
          <table className="table-header">
            <tr>
                <th className="cell">Monday</th>
                <th className="cell">Tuesday</th>
                <th className="cell">Wednesday</th>
                <th className="cell">Thursday</th>
                <th className="cell">Friday</th>
                <th className="cell">Saturday</th>
                <th className="cell">Sunday</th>
            </tr>
          </table>
          <Calender
            today={this.state.today}
            communityName={this.props.communityName}
          />
      </div>
    );
  }
}

export default Home;
