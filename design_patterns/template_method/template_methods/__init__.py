class teme_PermissionChecker:
    def check_required(self):
        raise NotImplementedError("teme_PermissionChecker.check_state must be implemented")
    def check_sufficient(self):
        raise NotImplementedError("teme_PermissionChecker.check_visitor must be implemented")
    def check_permission(self):
        if self.check_sufficent(): return True
        elif self.check_required(): return True
        else: return False