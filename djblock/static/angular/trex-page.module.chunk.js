webpackJsonp(["trex-page.module"],{

/***/ "./src/app/trex-page/trex-page-routing.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TrexPageRoutingModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("./node_modules/@angular/router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__core_services_auth_guard_service__ = __webpack_require__("./src/app/core/services/auth-guard.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__trex_page_component__ = __webpack_require__("./src/app/trex-page/trex-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var routes = [
    {
        path: '',
        canActivate: [__WEBPACK_IMPORTED_MODULE_2__core_services_auth_guard_service__["a" /* AuthGuardService */]],
        component: __WEBPACK_IMPORTED_MODULE_3__trex_page_component__["a" /* TrexPageComponent */]
    }
];
var TrexPageRoutingModule = /** @class */ (function () {
    function TrexPageRoutingModule() {
    }
    TrexPageRoutingModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */].forChild(routes)],
            exports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */]]
        })
    ], TrexPageRoutingModule);
    return TrexPageRoutingModule;
}());



/***/ }),

/***/ "./src/app/trex-page/trex-page.component.html":
/***/ (function(module, exports) {

module.exports = "<p>\n  trex-page works!\n</p>\n"

/***/ }),

/***/ "./src/app/trex-page/trex-page.component.scss":
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/trex-page/trex-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TrexPageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var TrexPageComponent = /** @class */ (function () {
    function TrexPageComponent() {
    }
    TrexPageComponent.prototype.ngOnInit = function () {
    };
    TrexPageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-trex-page',
            template: __webpack_require__("./src/app/trex-page/trex-page.component.html"),
            styles: [__webpack_require__("./src/app/trex-page/trex-page.component.scss")]
        }),
        __metadata("design:paramtypes", [])
    ], TrexPageComponent);
    return TrexPageComponent;
}());



/***/ }),

/***/ "./src/app/trex-page/trex-page.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TrexPageModule", function() { return TrexPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common__ = __webpack_require__("./node_modules/@angular/common/esm5/common.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__trex_page_routing_module__ = __webpack_require__("./src/app/trex-page/trex-page-routing.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__trex_page_component__ = __webpack_require__("./src/app/trex-page/trex-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var TrexPageModule = /** @class */ (function () {
    function TrexPageModule() {
    }
    TrexPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [
                __WEBPACK_IMPORTED_MODULE_1__angular_common__["b" /* CommonModule */],
                __WEBPACK_IMPORTED_MODULE_2__trex_page_routing_module__["a" /* TrexPageRoutingModule */]
            ],
            declarations: [__WEBPACK_IMPORTED_MODULE_3__trex_page_component__["a" /* TrexPageComponent */]]
        })
    ], TrexPageModule);
    return TrexPageModule;
}());



/***/ })

});
//# sourceMappingURL=trex-page.module.chunk.js.map