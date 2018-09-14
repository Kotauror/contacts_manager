import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import requestAnimationFrame from './shim';

Enzyme.configure({ adapter: new Adapter(), disableLifecycleMethods: true });
