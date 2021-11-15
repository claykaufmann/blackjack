import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value, suit, visibility } = data;

  let card = <></>;

  if (visibility === false) {
    card = <>backside of card</>;
  } else {
    card = (
      <>
        {value} of {suit}
      </>
    );
  }

  return (
    <div className="Card">
      <p className="Card-main">{card}</p>
    </div>
  );
};

export default Card;
