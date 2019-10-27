import React from 'react';
import './Header.css';
class Header extends React.Component {
  constructor(props) {
    super(props);
  }

  // setDateBounds = (d) => {
  //   d = new Date(d);
  //   var day = d.getDay();
  //   var diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
  //   // this.props.setMunday(new Date(d.setDate(diff)));
  //   // this.props.setSunday(new Date(d.setDate(6+diff)));
  // }

  // componentDidMount = () => {
  //   this.setDateBounds(this.props.today);
  // }

  // componentDidUpdate = () => {
  //   this.setDateBounds(this.props.today);
  // }

  getSunday(d) {
    d = new Date(d);
    var day = d.getDay();
    var diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(6+diff));
  }

  getMonday(d) {
    d = new Date(d);
    var day = d.getDay();
    var diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
    return new Date(d.setDate(diff));
  }

  render() {
    var monday = this.getMonday(this.props.today);
    var sunday = this.getSunday(this.props.today);
    return (
      <div className="header-container">
          <button className="prev-week-button" onClick={() => this.props.changeweek(-7)}><i className="left"></i></button>
          <div className="week-currently-viewing">
            {monday.getDate().toString()+"/"+monday.getMonth().toString()+"/"+monday.getFullYear().toString()+"  "} - 
            {"  "+sunday.getDate().toString()+"/"+sunday.getMonth().toString()+"/"+sunday.getFullYear().toString()}
          </div>
          <button className="next-week-button" onClick={() => this.props.changeweek(7)}><i className="right"></i></button>
          <button className="btn btn-secondary add-event">Add Event</button>
      </div>
    );
  }
}

export default Header;
