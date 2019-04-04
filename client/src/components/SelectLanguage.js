import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const styles = theme => ({
  tabsIndicator: {
    backgroundColor: 'blue'
  },

  tabSelected: {
    color: 'blue',
  },
});

const SelectLanguage = (props) => {
  const { classes } = props;

  const handleChange = (e) => {
    props.changeLang(e.target.textContent);
  }

  return (
    <Fragment>
      <Tabs
        value={props.value}
        variant='scrollable'
        scrollButtons='auto'
        style={{borderBottom: '1px solid #e8e8e8',}}
        classes={{ indicator: classes.tabsIndicator }}
      >

      {
        props.languages.map( (language) =>
          <Tab
            label={language}
            onClick={handleChange}
            style={{fontWeight: 700, fontSize: 15}}
            classes={{ selected: classes.tabSelected }}/>
        )
      }
      </Tabs>
    </Fragment>
  );
}

SelectLanguage.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SelectLanguage);
