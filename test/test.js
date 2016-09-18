// chai assertation library
const chai = require('chai'),
  expect = chai.expect
const path = require('path')
var sample = require(path.join('..', 'lib', 'sample'))


//==============================================
suite('Sample test for CI build', function() {


  //==============================================
  suite('Test suite 1', function() {
    var foo;
    setup(() => {
      foo = 1
    })
    test('foo is 1', () => {
      expect(foo).to.equal(1)
    })
  })
})
