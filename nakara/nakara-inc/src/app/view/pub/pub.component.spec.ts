import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PubComponent } from './pub.component';

describe('PubComponent', () => {
  let component: PubComponent;
  let fixture: ComponentFixture<PubComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PubComponent]
    });
    fixture = TestBed.createComponent(PubComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
