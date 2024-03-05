import createPushNotificationsJobs from './8-job.js'
const kue = require('kue')
const queue = kue.createQueue()
import { expect } from "chai";

describe('createPushNotificationsJobs', () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit()
  });

  it("...", () => {
    const job = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    };
    expect(() => {
      createPushNotificationsJobs(job, queue);
    }).to.throw(Error, 'Jobs is not an array');
  });

  it("...", () => {
    const job = {
      phoneNumber: '4153518781',
      message: 'This is the code 1234 to verify your account',
    };
    expect(() => {
      createPushNotificationsJobs(job, queue);
    }).to.throw(Error, 'Jobs is not an array');
  });

  it("...", () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw("Jobs is not an array");
  });

  it("...", () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw("Jobs is not an array");
  });

  it("...", () => {
    expect(() => {
      createPushNotificationsJobs("Hello", queue);
    }).to.throw("Jobs is not an array");
  });
});