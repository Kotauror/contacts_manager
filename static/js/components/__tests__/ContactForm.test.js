import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import fetch from 'isomorphic-fetch'

Enzyme.configure({adapter: new Adapter()});

import ContactForm from '../ContactForm.react';

describe('ContactForm', () => {
  const contactForm = shallow(<ContactForm />);

  it('renders correctly', () => {
    expect(contactForm).toMatchSnapshot();
  });

  it('initializes the state with empty name and telephone', () => {
    expect(contactForm.state().name).toEqual("");
    expect(contactForm.state().telephone).toEqual("");
  });
});
