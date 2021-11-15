import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value, suit, visibility } = data;

  let card = <></>;

  if (visibility === false) {
    card = (
      <>
        <p className="Card-backside" />
      </>
    );
  } else {
    card = (
      <>
        <p className="Card-front">
          {value} of {suit}
        </p>
      </>
    );
  }

  return <div className="Card">{card}</div>;
};

export default Card;
