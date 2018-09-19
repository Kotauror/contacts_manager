import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import fetch from 'isomorphic-fetch'
import { mount } from 'enzyme';

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

  describe('when typing into name and telephone input', () => {

    beforeEach(() => {
      contactForm.find('.input-name').simulate('change', { target: { value: "Justyna"}});
      contactForm.find('.input-phone').simulate('change', { target: { value: "111"}});
    });

    it('updates the name in state', () => {
      expect(contactForm.state().name).toEqual("Justyna");
    });

    it('updates the phone in state', () => {
      expect(contactForm.state().telephone).toEqual("111");
    });
  })
});
