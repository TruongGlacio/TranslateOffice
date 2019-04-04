import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
    width: 150,
    fontWeight: 600
  },
  input: {
    display: 'none',
  },
});

const NavButton = (props) => {
  const { classes } = props;

  const handleClick = (e) => {
    if(e.target.textContent.match('ext') != null) {
      props.changeScreen('Text');
    } else {
      props.changeScreen('Document');
    }
  }

  return (
    <div style={{margin: 20}}>
      <Button variant='contained' color='primary' className={classes.button} onClick={handleClick}>
        <Icon>text_fields</Icon>
        Text
      </Button>
      <Button variant='contained' className={classes.button} onClick={handleClick}>
        <Icon>description</Icon>
        Document
      </Button>
    </div>
  );
}

NavButton.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(NavButton);
