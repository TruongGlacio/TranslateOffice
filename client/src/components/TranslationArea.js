import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import classNames from 'classnames';
import Divider from '@material-ui/core/Divider';
import Paper from '@material-ui/core/Paper';
import InputLanguague from './InputLanguage';
import Grid from '@material-ui/core/Grid';
import OutputLanguage from './OutputLanguage';
import SelectLanguage from './SelectLanguage';
import UploadArea from './UploadArea';
import IconButton from '@material-ui/core/IconButton';
import { Icon } from '@material-ui/core';

const styles = theme => ({
  root: {
    flexGrow: 1,
  },

  verticalLine: {
    borderLeft: `2px solid ${theme.palette.divider}`,
  },

  GridItem: {
    padding: 20,
  },
});

const TranslationArea = (props) => {
  const { classes } = props;

  const changeInputLang = (inputLang) => {
    props.changeInputLang(inputLang);
  }

  const changeOutputLang = (outputLang) => {
    props.changeOutputLang(outputLang);
  }

  const handleClick = () => {
    props.swapLang()
  }

  let view;
  if (props.screen === 'Text') {
    view =
      <Fragment>
        <Grid item xs={12} sm={6} className={classes.GridItem}>
          <InputLanguague changeInput={props.changeTextInput} />
        </Grid>
        <Grid item xs={12} sm={6} className={classNames(classes.GridItem, classes.verticalLine)}>
          <OutputLanguage text={props.text} />
        </Grid>
      </Fragment>
  } else {
    view =
      <Grid item xs={12} sm={12} className={classes.GridItem}>
        <UploadArea />
      </Grid>
  }

  return (
    <div className={classes.root}>
      <Paper style={{margin: 20}}>
        <Grid container>
          <Grid item xs={12}>
            <Grid container>
              <Grid item xs={12} sm={5}>
                <SelectLanguage
                  changeLang={changeInputLang}
                  languages={props.languages}
                  value={props.langValues.input} />
              </Grid>
              <Grid item xs={2} sm={2} style={{textAlign: 'center'}}>
                <IconButton  onClick={handleClick}>
                  <Icon>swap_horiz</Icon>
                </IconButton>
              </Grid>
              <Grid item xs={12} sm={5} >
              <SelectLanguage
                changeLang={changeOutputLang}
                languages={props.languages}
                value={props.langValues.output} />
              </Grid>
            </Grid>
          <Divider />
          </Grid>
          {view}
        </Grid>
      </Paper>
    </div>
  );
}

TranslationArea.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(TranslationArea);
