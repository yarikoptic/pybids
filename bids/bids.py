from __future__ import absolute_import, division, print_function

from .due import due, Doi

__all__ = []


# Use duecredit (duecredit.org) to provide a citation to relevant work to
# be cited. This does nothing, unless the user has duecredit installed,
# And calls this with duecredit (as in `python -m duecredit script.py`):
due.cite(Doi("10.1038/sdata.2016.44"),
         description="Brain Imaging Data Structure",
         tags=["reference-implementation"],
         path='bids')


#
# Hm.... with all the optional session leveling becomes trickyish to
# come up with a consistent OOP API to access specific modality.
# Should we always assume having a dict of sessions or ... ?
# With func-based API we could simply assume session=None
# unless explicitly specified

class BIDSDataset(object):

    sessions = {None: Session()}

    @property
    def session_labels(self):
        return list(self.sessions)

    @property
    def is_single_session(self):
        return self.sessions and list(self.sessions) == [None]

    @property
    def is_multi_session(self):
        return self.sessions and list(self.sessions) != [None]


    #
    # Subjects
    #

    subjects = {'001': Subject()}

    @property
    def subject_labels(self):
        return list(self.subjects)

    #
    # Introspection of subjects' content
    #

    def get_modality_labels(self, subjects=None, sessions=None):
        """Return list of present modality labels

        Parameters
        ----------
        subjects: list of str, optional
          If provided, would specify which particular sessions to consider.
          If None -- all
        sessions: list of str, optional
          If provided, would specify which particular sessions to consider.
          If None -- all

        Returns
        -------
        list of str
        """
        return sorted(
            for session in (sessions or self.session_labels)
            for subject in (subjects or self.subject_labels)
        )

    #
    # Manipulation helpers (ideas)
    #
    def select(self, subjects=None, sessions=None):
        """Sub-select the dataset"""
        raise NotImplementedError
        return Dataset()

    # crazy one - may be not worth it!
    def __getattribute__(self, item):
        """Allow to do (later) fancy completions in ipython etc

        ds.sub_control01.
        ds.sess_pre.
        """
        if '_' in item:
            t, label = item.split('_', 1)
            if t == 'sub':
                return self.subjects[label]
            elif t == 'sess':
                return self.sessions[label or None]
        return super(BIDSDataset, self).__getattribute__(item)


class Session(object):
    pass

class Subject(object):
    pass
