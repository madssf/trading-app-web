import React, { Component, useState } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";
import {getCurrencies} from '../../../store/CurrenciesActions'
import Currency from './Currency'


class CurrenciesList extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      sortedfield: "mcap_rank",
    };
  }
  componentDidMount() {
    this.props.getCurrencies();
    
  }

  render() {
    const {currencies} = this.props.currencies
    const {sorted_by} = this.state.sortedfield
    if (currencies.length === 0){
      return <p>No currencies yet.</p>
    }

    let sorted_currencies = [...currencies];
    if (sorted_currencies !== null) {
      sorted_currencies.sort((a,b) => {
        if (a[sorted_by] < b[sorted_by]) {
          return -1;
        }
        if (a[sorted_by] > b[sorted_by]) {
          return 1;
        }
        return 0;
      }) 
    }
   

    return (
          <Container>
          <div> 
          <h1>Currencies</h1>
          <p>Displaying {sorted_currencies.length} currencies</p>
            <table>
              <caption>Currencies</caption>
 
            <thead>
              <tr>
              <th>
                  <button type="button" onClick={() => this.setState({sortedfield: 'mcap_rank'})} >
                    Rank
                  </button>
                </th>                  
                <th>
                  <button type="button" onClick={() => this.setState({sortedfield: 'symbol'})} >
                    Symbol
                  </button>
                </th>
                <th>
                  <button type="button" onClick={() => this.setState({sortedfield: 'name'})} >
                    Name
                  </button>
                </th>               
                <th>
                  <button type="button" onClick={() => this.setState({sortedfield: 'last_price'})} >
                    Price
                  </button>
                </th>                
                <th>
                  <button type="button" onClick={() => this.setState({sortedfield: 'pct_change_24h'})} >
                    % 24h
                  </button>
                </th>
              </tr>
            </thead>
              <tbody>
            {sorted_currencies.map(currency => (
              <tr key={currency.id}>
                <td>{currency.mcap_rank}</td>
                <td>{currency.symbol}</td>
                <td>{currency.name}</td>
                <td>{currency.last_price}</td>
                <td>{currency.pct_change_24h}</td>
              </tr>
            ))}
          </tbody>
           </table>
          </div> 
          </Container>
  );
}
}

CurrenciesList.propTypes = {
  currencies: PropTypes.object.isRequired,
  getCurrencies: PropTypes.func.isRequired,
};

const mapStateToProps = state => ({
  currencies: state.currencies,
});

export default connect(mapStateToProps, {getCurrencies})(withRouter(CurrenciesList));

const useSortableData = (items, config = null) => {
  const [sortConfig, setSortConfig] = React.useState(config);
  
  const sortedItems = React.useMemo(() => {
    let sortableItems = [...items];
    if (sortConfig !== null) {
      sortableItems.sort((a, b) => {
        if (a[sortConfig.key] < b[sortConfig.key]) {
          return sortConfig.direction === 'ascending' ? -1 : 1;
        }
        if (a[sortConfig.key] > b[sortConfig.key]) {
          return sortConfig.direction === 'ascending' ? 1 : -1;
        }
        return 0;
      });
    }
    return sortableItems;
  }, [items, sortConfig]);

  const requestSort = key => {
    let direction = 'ascending';
    if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    setSortConfig({ key, direction });
  }

  return { items: sortedItems, requestSort };
}
